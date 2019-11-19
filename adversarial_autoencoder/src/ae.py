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

# VAE model
class AE(nn.Module):
    def __init__(self, img_size=784, h_dim=400, z_dim=20):
        super(AE, self).__init__()
        self.fc1 = nn.Linear(img_size, h_dim)
        self.fc2 = nn.Linear(h_dim, z_dim)
        self.fc3 = nn.Linear(z_dim, h_dim)
        self.fc4 = nn.Linear(h_dim, img_size)

    def encode(self, x):
        h = F.relu(self.fc1(x))
        z = self.fc2(h)
        return z
    
    def decode(self, z):
        h = F.relu(self.fc3(z))
        x = self.fc4(h)
        return torch.sigmoid(x)

    def forward(self, x):
        z = self.encode(x)
        x_reconst = self.decode(z)
        kwouts = {'z': z}
        return x_reconst, kwouts

    def compute_loss(self, x):
        x_reconst, kwouts = self(x)
        z = kwouts["z"]
        mse_loss = F.mse_loss(x_reconst, x)
        return mse_loss

model = AE(img_size=img_size, h_dim=h_dim, z_dim=z_dim).to(device)

optimizer = torch.optim.Adam(model.parameters(), lr=lr)

for epoch in range(1, epochs+1):
    model.train()
    total_loss = 0.
    for i, (x, _) in enumerate(train_loader):
        x = x.to(device).view(-1, img_size)
        loss = model.compute_loss(x)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
    print("Epoch: {}, Loss: {:.4f}".format(epoch, total_loss))

    # Show reconstruction
    model.eval()
    with torch.no_grad():
        x, _ = next(iter(test_loader))
        x = x.to(device).view(-1, img_size)
        x_reconst, _ = model(x)
        x_reconst = make_grid(x_reconst.view(-1, 1, img_width, img_width))
        x_reconst = x_reconst.data.cpu().numpy().transpose(1, 2, 0)
        x_reconst = np.clip(x_reconst, 0, 1)
        x = make_grid(x.view(-1, 1, img_width, img_width))
        x = x.data.cpu().numpy().transpose(1, 2, 0)
        x = np.clip(x, 0, 1)

        fig = plt.figure(figsize=(10, 8))
        plt.suptitle("Epoch: {}".format(epoch))
        plt.subplot(121)
        plt.imshow(x_reconst)
        plt.title("Reconstruction")
        plt.axis("off")
        plt.subplot(122)
        plt.imshow(x)
        plt.title("Origin")
        plt.axis("off")
        plt.savefig("comp_ae.png")
        plt.show()

# See distribution in the 2-D space
model.eval()
zs, ts = [], []
for x, t in test_loader:
    with torch.no_grad():
        x = x.to(device).view(-1, img_size)
        x_reconst, kwouts = model(x)
        z = kwouts['z']
        zs.append(z.data.cpu())
        ts.append(t)
zs = torch.cat(zs, dim=0)
ts = torch.cat(ts, dim=0)
visualize_z(zs, ts, figsize=(8, 8), fname="tsne_ae.png")

