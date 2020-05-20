"""
https://mc.ai/part-2-bert-fine-tuning-tutorial-with-pytorch-for-text-classification-on-the-corpus-of-linguistic/
"""
import torch
from transformers import BertTokenizer
from torch.nn.utils.rnn import pad_sequence
from sklearn.model_selection import train_test_split
from torch.utils.data import (
    TensorDataset,
    DataLoader,
    RandomSampler,
    SequentialSampler,
)  # The DataLoader needs to know our batch size for training, so we specify it
from transformers import (
    BertForSequenceClassification,
    AdamW,
    BertConfig,
)  # Load BertForSequenceClassification, the pretrained BERT model with a single
from transformers import get_linear_schedule_with_warmup
import numpy as np  # Function to calculate the accuracy of our predictions vs labels
import pandas as pd  # Load the dataset into a pandas dataframe.
import time
import random
import datetime

RANDOM_SEED = 40
random.seed(RANDOM_SEED)
np.random.seed(RANDOM_SEED)
torch.cuda.manual_seed_all(RANDOM_SEED)


def format_time(elapsed):
    """
    Takes a time in seconds and returns a string hh:mm:ss
    """
    # Round to the nearest second.
    elapsed_rounded = int(round((elapsed)))

    # Format as hh:mm:ss
    return str(datetime.timedelta(seconds=elapsed_rounded))


def flat_accuracy(preds, labels):
    pred_flat = np.argmax(preds, axis=1).flatten()
    labels_flat = labels.flatten()
    return np.sum(pred_flat == labels_flat) / len(labels_flat)


path = "../../datasets/cola_public/raw/in_domain_train.tsv"
df = pd.read_csv(
    path,
    delimiter="\t",
    header=None,
    names=["sentence_source", "label", "label_notes", "sentence"],
)  # Report the number of sentences.
print(
    "Number of training sentences: {:,}\n".format(df.shape[0])
)  # Display 10 random rows from the data.

# Get the lists of sentences and their labels
sentences = df.sentence.values
labels = df.label.values

# Add special tokens to the start and end of each sentence
# Pad & truncate all sentences to a single constant length
# Explicitly differentiate real tokens from padding tokens with the attention mask
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased", do_lower_case=True)
input_ids = []
for sent in sentences:
    encoded_sent = tokenizer.encode(sent, add_special_tokens=True, return_tensors="pt")
    input_ids.append(encoded_sent.squeeze())

print("Original: {}".format(sentences[0]))
print("Token IDs: {}".format(input_ids[0]))

# Padding
input_ids = pad_sequence(input_ids, batch_first=True, padding_value=0)

# Attention masks
attention_masks = []
for sent in input_ids:
    att_mask = [int(token_id > 0) for token_id in sent]
    attention_masks.append(att_mask)

# Train test split
train_inputs, val_inputs, train_labels, val_labels = train_test_split(
    input_ids.numpy(), labels, random_state=2020, test_size=0.1
)
train_masks, val_masks, _, _ = train_test_split(
    attention_masks, labels, random_state=2020, test_size=0.1
)

# Prepare dataloader
train_inputs = torch.tensor(train_inputs)
train_labels = torch.tensor(train_labels)
val_inputs = torch.tensor(val_inputs)
val_labels = torch.tensor(val_labels)
train_masks = torch.tensor(train_masks)
val_masks = torch.tensor(val_masks)

train_data = TensorDataset(train_inputs, train_masks, train_labels)
train_dataloader = DataLoader(train_data, batch_size=16, shuffle=True)
val_data = TensorDataset(val_inputs, val_masks, val_labels)
val_dataloader = DataLoader(val_data, batch_size=32, shuffle=False)

# Define BERT Model
model = BertForSequenceClassification.from_pretrained(
    "bert-base-uncased",
    num_labels=2,
    output_attentions=False,
    output_hidden_states=False,
)
model.cuda()
# Get all of the model's parameters as a list of tuples.
params = list(model.named_parameters())
print("The BERT model has {:} different named parameters.\n".format(len(params)))
print("==== Embedding Layer ====\n")
for p in params[0:5]:
    print("{:<55} {:>12}".format(p[0], str(tuple(p[1].size()))))
print("\n==== First Transformer ====\n")
for p in params[5:21]:
    print("{:<55} {:>12}".format(p[0], str(tuple(p[1].size()))))
print("\n==== Output Layer ====\n")
for p in params[-4:]:
    print("{:<55} {:>12}".format(p[0], str(tuple(p[1].size()))))

# Optimizer
optimizer = AdamW(model.parameters(), lr=2e-5, eps=1e-8,)
epochs = 4
total_steps = len(train_dataloader) * epochs
scheduler = get_linear_schedule_with_warmup(
    optimizer, num_warmup_steps=0, num_training_steps=total_steps
)

# Train loop
loss_values = []
for epoch in range(epochs):
    # Training
    print("======== Epoch {:} / {:} ========".format(epoch + 1, epochs))
    print("Training...")  # Measure how long the training epoch takes.
    t0 = time.time()  # Reset the total loss for this epoch.
    total_loss = 0  # Put the model into training mode. Don't be mislead--the call to
    model.train()
    for step, batch in enumerate(train_dataloader):
        # Unpack this training batch from our dataloader.
        b_input_ids = batch[0].cuda()
        b_input_mask = batch[1].cuda()
        b_labels = batch[2].cuda()
        output = model(
            b_input_ids,
            token_type_ids=None,
            attention_mask=b_input_mask,
            labels=b_labels,
        )
        loss = output[0]
        total_loss += loss.item()
        loss.backward()
        torch.nn.utils.clip_grad_norm_(
            model.parameters(), 1.0
        )  # Update parameters and take a step using the computed gradient.
        optimizer.step()
        scheduler.step()
        loss_values.append(loss.item())
        if step % 100 == 0 and step != 0:
            elapsed = format_time(time.time() - 50)
            print(
                " Batch {:>5,} of {:>5,}. Elapsed: {:}. Loss: {:.4f}".format(
                    step, len(train_dataloader), elapsed, loss.item()
                )
            )
    avg_train_loss = total_loss / len(train_dataloader)

    # Store the loss value for plotting the learning curve.
    print()
    print(" Average training loss: {0:.2f}".format(avg_train_loss))
    print(" Training epcoh took: {:}".format(format_time(time.time() - t0)))

    # Validation
    # After the completion of each training epoch, measure our performance on
    # our validation set. print("")
    print("Running Validation...")
    t0 = (
        time.time()
    )  # Put the model in evaluation mode--the dropout layers behave differently
    # during evaluation.
    model.eval()  # Tracking variables
    eval_loss, eval_accuracy = 0, 0
    nb_eval_steps, nb_eval_examples = 0, 0  # Evaluate data for one epoch
    for batch in val_dataloader:
        # Add batch to GPU
        batch = tuple(t.cuda() for t in batch)

        # Unpack the inputs from our dataloader
        b_input_ids, b_input_mask, b_labels = batch
        with torch.no_grad():
            outputs = model(
                b_input_ids, token_type_ids=None, attention_mask=b_input_mask
            )

        logits = outputs[0]  # Move logits and labels to CPU
        logits = logits.detach().cpu().numpy()
        label_ids = b_labels.to("cpu").numpy()

        # Calculate the accuracy for this batch of test sentences.
        tmp_eval_accuracy = flat_accuracy(logits, label_ids)

        # Accumulate the total accuracy.
        eval_accuracy += tmp_eval_accuracy  # Track the number of batches
        nb_eval_steps += 1  # Report the final accuracy for this validation run.
    print(" Accuracy: {0:.2f}".format(eval_accuracy / nb_eval_steps))
    print(" Validation took: {:}".format(format_time(time.time() - t0)))
    print()
print("Training complete!")
#TODO
# MCC evaluation
