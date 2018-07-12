import numpy as np
np.random.seed(123)  # for reproducibility
 
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPool2D
from keras.utils import np_utils
from keras.datasets import mnist
from keras.callbacks import EarlyStopping, ModelCheckpoint
 
# 4. Load pre-shuffled MNIST data into train and test sets
(X_train, y_train), (X_test, y_test) = mnist.load_data()
 
# 5. Preprocess input data
X_train = X_train.reshape(X_train.shape[0], 1, 28, 28)
X_test = X_test.reshape(X_test.shape[0], 1, 28, 28)
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train /= 255
X_test /= 255
 
# 6. Preprocess class labels
Y_train = np_utils.to_categorical(y_train, 10)
Y_test = np_utils.to_categorical(y_test, 10)
 
# 7. Define model architecture
model = Sequential()
 
model.add(Flatten(input_shape=(1, 28, 28)))
model.add(Dense(256, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(256, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(10))
model.add(Activation('softmax'))
fBestModel = 'best_model.h5'
early_stop = EarlyStopping(monitor='val_loss', patience=2, verbose=1)
best_model = ModelCheckpoint(fBestModel, verbose=0, save_best_only=True)
 
# 8. Compile model
model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
 
# 9. Fit model on training data
model.summary()
network_history = \
model.fit(X_train, Y_train, 
          validation_data = (X_test, Y_test),
          batch_size=32, epochs=5, verbose=1,
          callbacks=[best_model, early_stop])
 
print(network_history.history)
# 10. Evaluate model on test data
score = model.evaluate(X_test, Y_test, verbose=0)
print(score)

######################################################################
model_truncated = Sequential()
model_truncated.add(Flatten(input_shape=(1, 28, 28)))
model_truncated.add(Dense(256, activation='relu'))
model_truncated.add(Dropout(0.2))
model_truncated.add(Dense(256))
# Load weights
for i, layer in enumerate(model_truncated.layers):
    layer.set_weights(model.layers[i].get_weights())

model_truncated.compile(loss='categorical_crossentropy',
                        optimizer='adam',
                        metrics=['accuracy'])

# Check
print(np.all(model_truncated.layers[1].get_weights()[0] == model.layers[1].get_weights()[0]))

hidden_features = model_truncated.predict(X_train)
print(hidden_features.shape)

# TSNE
from sklearn.manifold import TSNE
tsne = TSNE(n_components=2)
X_tsne = tsne.fit_transform(hidden_features[:1000])
colors_map = np.argmax(Y_train, axis=1)
print(np.where(colors_map==6))

# Plot
import matplotlib.pyplot as plt
colors = np.array([x for x in 'b-g-r-c-m-y-k-purple-coral-lime'.split('-')])
colors_map = colors_map[:1000]
plt.figure(figsize=(10, 10))
for cl in range(10):
    indices = np.where(colors_map==cl)
    plt.scatter(X_tsne[indices, 0], X_tsne[indices, 1], c=colors[cl], label=cl)
plt.legend()
plt.show()

# Use Bokeh to plot interactive figure
from bokeh.plotting import figure, show
p = figure(plot_width=600, plot_height=600)
colors = [x for x in 'blue-green-red-cyan-magenta-yellow-black-purple-coral-lime'.split('-')]
colors_map = colors_map[:1000]
for cl in range(10):
    indices = np.where(colors_map == cl)
    p.circle(X_tsne[indices, 0].ravel(), X_tsne[indices, 1].ravel(), size=7,
             color=colors[cl], alpha=0.4, legend=str(cl))
p.legend.location = 'bottom_right'
show(p)

# Try more
# Use plotly to plot 3D TSNE figure?
# Use another algorithm to create the manifold sklearn.manifold.MDS?
# https://www.youtube.com/watch?v=FrkYu2zVUyM
