
# coding: utf-8

# In[1]:


import torchvision
import torch
import numpy as np
import matplotlib.pyplot as plt
from torch.utils.data import DataLoader
import torch.nn as nn
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


transform = torchvision.transforms.Compose([
    torchvision.transforms.ToTensor(),
])
train_dataset = torchvision.datasets.FashionMNIST('/export/home/wangx/datasets/fashion-mnist/',
                                                  train=True,
                                                  download=True,
                                                  transform=transform)

test_dataset = torchvision.datasets.FashionMNIST('/export/home/wangx/datasets/fashion-mnist/',
                                                 train=False,
                                                 download=True,
                                                 transform=transform)


# In[3]:


BATCH_SIZE = 64
train_loader = DataLoader(train_dataset, shuffle=True, batch_size=BATCH_SIZE)
test_loader = DataLoader(test_dataset, shuffle=True, batch_size=BATCH_SIZE)


# In[4]:


batch = next(iter(train_loader))
print(batch[0].shape, batch[1].shape)


# In[5]:


N_IDEAS = 16
ART_COMPONENTS = 28*28

G = nn.Sequential(                      # Generator
    nn.Linear(N_IDEAS+1, 128),          # random ideas (could from normal distribution) + class label
    nn.ReLU(),
    nn.Linear(128, ART_COMPONENTS),     # making a painting from these random ideas
)

D = nn.Sequential(                      # Discriminator
    nn.Linear(ART_COMPONENTS+1, 128),   # receive art work either from the famous artist or a newbie like G with label
    nn.ReLU(),
    nn.Linear(128, 1),
    nn.Sigmoid(),                       # tell the probability that the art work is made by artist
)


# In[6]:


LR_D = 1e-4
LR_G = 1e-4
opt_D = torch.optim.Adam(D.parameters(), lr=LR_D)
opt_G = torch.optim.Adam(G.parameters(), lr=LR_G)


# | Label | Description |
# | --- | --- |
# | 0 | T-shirt/top |
# | 1 | Trouser |
# | 2 | Pullover |
# | 3 | Dress |
# | 4 | Coat |
# | 5 | Sandal |
# | 6 | Shirt |
# | 7 | Sneaker |
# | 8 | Bag |
# | 9 | Ankle boot |

# In[7]:


def visualize(which_one=1.):
    z = torch.randn(16, N_IDEAS).to(device)
    label = torch.ones((16, 1)).to(device)
    label = label * which_one
    G_iputs = torch.cat((z, label), 1)
    G_paints = G(G_iputs)
    G_paints = G_paints.reshape(16, 1, 28, 28)

    image = torchvision.utils.make_grid(G_paints, normalize=True)
    plt.imshow(image.cpu().detach().numpy().transpose((1,2 ,0)))
    plt.axis('off')
    plt.show()


# In[11]:


device = torch.device('cuda:0')
G = G.to(device)
D = D.to(device)

for epoch in range(1, 10+1):
    for n, (images, labels) in enumerate(train_loader, 1):
        images = images.reshape(-1, 28*28).to(device)
        labels = labels.unsqueeze(dim=-1).float().to(device)
        
        G_ideas = torch.randn(images.shape[0], N_IDEAS).to(device)
        G_inputs = torch.cat((G_ideas, labels), 1) # (64, 17)
        G_paints = G(G_inputs)
        
        D_inputs0 = torch.cat((images, labels), 1)
        D_inputs1 = torch.cat((G_paints, labels), 1)
        prob_artist0 = D(D_inputs0) # D try to increase this prob
        prob_artist1 = D(D_inputs1) # D try to reduce this prob
        
        D_score0 = torch.log(prob_artist0)
        D_score1 = torch.log(1. - prob_artist1)
        D_loss = -torch.mean(D_score0 + D_score1)
        G_loss = torch.mean(D_score1) # G try to maximize this loss
        
        opt_D.zero_grad()
        D_loss.backward(retain_graph=True)
        opt_D.step()
        
        opt_G.zero_grad()
        G_loss.backward()
        opt_G.step()
        
        if n % 300 == 0:
            print("# {}, D_loss: {:.4f}, G_loss: {:.4f}".format(n, D_loss.item(), G_loss.item()))
    
    print("Epoch: {}".format(epoch))
    visualize(9.)

