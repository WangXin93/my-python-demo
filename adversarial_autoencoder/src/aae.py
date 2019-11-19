# https://medium.com/m/global-identity?redirectUrl=https%3A%2F%2Ftowardsdatascience.com%2Fa-wizards-guide-to-adversarial-autoencoders-part-2-exploring-latent-space-with-adversarial-2d53a6f8a4f9
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
class AAE(nn.Module):
    def __init__(self, img_size=784, h_dim=400, z_dim=20):
        super(AAE, self).__init__()
        self.fc1 = nn.Linear(img_size, h_dim)
        self.fc2 = nn.Linear(h_dim, z_dim)
        self.fc3 = nn.Linear(z_dim, h_dim)
        self.fc4 = nn.Linear(h_dim, img_size)
        self.fc5 = nn.Linear(z_dim, h_dim)
        self.fc6 = nn.Linear(h_dim, 1)

    def encode(self, x):
        h = F.relu(self.fc1(x))
        z = self.fc2(h)
        return z
    
    def decode(self, z):
        h = F.relu(self.fc3(z))
        x = self.fc4(h)
        return torch.sigmoid(x)

    def discriminate(self, z):
        h = F.relu(self.fc5(z))
        score = torch.sigmoid(self.fc6(h))
        return score

    def forward(self, x):
        z = self.encode(x)
        x_reconst = self.decode(z)
        kwouts = {'z': z}
        return x_reconst, kwouts

    def compute_reconst_loss(self, x):
        x_reconst, kwouts = self(x)
        z = kwouts["z"]
        mse_loss = F.mse_loss(x_reconst, x)
        return mse_loss

    def compute_dc_loss(self, x):
        feat_real = torch.randn(batch_size, z_dim).to(device)
        feat_real = feat_real * 5
        feat_fake = self.encode(x)
        dc_real = self.discriminate(feat_real)
        dc_fake = self.discriminate(feat_fake.detach())
        dc_loss_real = F.binary_cross_entropy(
            dc_real, torch.ones_like(dc_real).to(device)
        )
        dc_loss_fake = F.binary_cross_entropy(
            dc_fake, torch.zeros_like(dc_fake).to(device)
        )
        dc_loss = dc_loss_real + dc_loss_fake
        return dc_loss
    
    def compute_gen_loss(self, x):
        feat_fake = self.encode(x)
        dc_fake = self.discriminate(feat_fake)
        g_loss = F.binary_cross_entropy(
            dc_fake, torch.ones_like(dc_fake).to(device)
        )
        return g_loss

model = AAE(img_size=img_size, h_dim=h_dim, z_dim=z_dim).to(device)

optimizer = torch.optim.Adam(model.parameters(), lr=lr)
D_parameters =  [p for n, p in model.named_parameters() if n in [
    'fc5.weight', 'fc5.bias', 'fc6.weight', 'fc6.bias']]
G_parameters =  [p for n, p in model.named_parameters() if n in [
    'fc1.weight', 'fc1.bias', 'fc2.weight', 'fc2.bias']]
optimizer_D = torch.optim.Adam(D_parameters, lr=lr)
optimizer_G = torch.optim.Adam(G_parameters, lr=lr)

for epoch in range(1, epochs+1):
    model.train()
    total_reconst_loss, total_dc_loss, total_gen_loss = 0., 0., 0.
    for i, (x, _) in enumerate(train_loader):
        # step1: train with reconstruction loss
        x = x.to(device).view(-1, img_size)
        loss = model.compute_reconst_loss(x)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        total_reconst_loss += loss.item()

        # step2: train the discriminator
        loss = model.compute_dc_loss(x)
        optimizer_D.zero_grad()
        loss.backward()
        optimizer_D.step()
        total_dc_loss += loss.item()

        # step3: train the generator
        loss = model.compute_gen_loss(x)
        optimizer_G.zero_grad()
        loss.backward()
        optimizer_G.step()
        total_gen_loss += loss.item()
    print("Epoch: {}, Rconst Loss: {:.4f}, DC Loss: {:.4f}, GEN Loss: {:.4f}".format(
        epoch, total_reconst_loss, total_dc_loss, total_gen_loss))

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
        plt.savefig("comp_aae.png")
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
visualize_z(zs, ts, figsize=(8, 8), fname="tsne_aae.png")

