import torch
import torchvision
import torch.nn as nn
import torch.nn.functional as F
from torchvision import transforms
from torch.utils.data import DataLoader, Dataset
from torchvision.utils import make_grid
from utils import visualize_z

import numpy as np
import matplotlib.pyplot as plt

# Hyper-parameters
img_width = 28
img_size = 784
h_dim = 1000
z_dim = 2
epochs = 15
batch_size = 128
lr = 1e-3

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

train_d = torchvision.datasets.MNIST(root='./data', train=True, transform=transforms.ToTensor(), download=False)
test_d = torchvision.datasets.MNIST(root='./data', train=False, transform=transforms.ToTensor(), download=False)

train_loader = DataLoader(train_d, batch_size, shuffle=True)
test_loader = DataLoader(test_d, batch_size, shuffle=False)

class PCA(object):
    def __init__(self, k=2):
        self.k = k
        self.U = None

    def encode(self, x):
        x_mean = torch.mean(x, 0)
        x = x - x_mean.expand_as(x)

        U, S, V = torch.svd(torch.t(x))
        self.U = U
        return torch.mm(x, U[:, :self.k])

    def decode(self, z):
        assert self.U is not None
        x = torch.mm(z, torch.t(self.U[:, :self.k]))
        return x

model = PCA(k=z_dim)

# Show reconstruction
xs = test_d.data.view(-1, img_size).float()
ts = test_d.targets
zs = model.encode(xs)
xs_reconst = model.decode(zs)

x_reconst = make_grid(xs_reconst[:batch_size].view(-1, 1, img_width, img_width))
x_reconst = x_reconst.data.cpu().numpy().transpose(1, 2, 0)
x_reconst = np.clip(x_reconst, 0, 1)
x = make_grid(xs[:batch_size].view(-1, 1, img_width, img_width))
x = x.data.cpu().numpy().transpose(1, 2, 0)
x = np.clip(x, 0, 1)

fig = plt.figure(figsize=(10, 8))
plt.suptitle("PCA")
plt.subplot(121)
plt.imshow(x_reconst)
plt.title("Reconstruction")
plt.axis("off")
plt.subplot(122)
plt.imshow(x)
plt.title("Origin")
plt.axis("off")
plt.savefig("comp_pca.png")
plt.show()

# See distribution in the 2-D space
visualize_z(zs, ts, figsize=(8, 8), fname="tsne_pca.png")