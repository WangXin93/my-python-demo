"""
visualize_z: visualize the projected points with class label in 2D space

Reference:
https://www.sambaiz.net/article/213/
https://www.sambaiz.net/article/201/
"""

from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

colors = ["red", "green", "blue", "orange", "purple", "brown", "fuchsia", "grey", "olive", "lightblue"]
def visualize_z(z, labels, figsize=(10, 10), colors=colors, fname=None):
    fig = plt.figure(figsize=(10, 10))
    if z.size(1) > 2:
        print("Run TSNE...")
        points = TSNE(n_components=2, random_state=2033).fit_transform(z)
    else:
        print("Data is 2D, skip TSNE...")
        points = z
    for p, l in zip(points, labels):
        plt.scatter(p[0], p[1], marker="${}$".format(l), c=colors[l])

    if fname is not None:
        plt.title(fname.split(".")[0].upper())
        plt.savefig(fname)
        print("Saved TSNE image to {}".format(fname))
    plt.show()


# x = np.linspace(-10, 10, 21)
# y = np.linspace(-10, 10, 21)
# to_decode = []
# for xv in x:
#     for yv in y:
#         to_decode.append((xv, yv))
# to_decode = torch.tensor(to_decode)
# to_decode = to_decode.to(device)
# output = autoencoder.decode(to_decode)
# output = output.view(-1, 1, 28, 28)
# show = torchvision.utils.make_grid(output, nrow=21)
# show = show.cpu().data.numpy()
# show = show.transpose((1, 2, 0))

# figure = plt.figure(figsize=(10, 10))
# plt.imshow(show)
# plt.show()