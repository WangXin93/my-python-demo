import networkx as nx
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import torch
import dgl
import imageio
import numpy as np

N = 50  # number of nodes
DAMP = 0.85  # damping factor
K = 10  # number of iterations
SEED = 9
ALPHA = 0.1
g = nx.nx.erdos_renyi_graph(N, 0.1, seed=SEED)
g = dgl.DGLGraph(g)

# g.ndata['pv'] = torch.ones(N) / N
g.ndata['pv'] = torch.zeros(N)
g.ndata['pv'][0] = 1
g.ndata['e'] = g.ndata['pv'].clone()
g.ndata['deg'] = g.out_degrees(g.nodes()).float()

# def pagerank_message_func(edges):
#     return {'pv' : edges.src['pv'] / edges.src['deg']}

# def pagerank_reduce_func(nodes):
#     msgs = torch.sum(nodes.mailbox['pv'], dim=1)
#     pv = (1 - DAMP) / N + DAMP * msgs
#     return {'pv' : pv}

# Naive random walk
# def pagerank_message_func(edges):
#     return {'pv' : edges.src['pv'] / edges.src['deg']}

# def pagerank_reduce_func(nodes):
#     msgs = torch.sum(nodes.mailbox['pv'], dim=1)
#     pv = msgs
#     return {'pv' : pv}

# Lazy random walk
# def pagerank_message_func(edges):
#     return {'pv' : edges.src['pv'] / edges.src['deg']}

# def pagerank_reduce_func(nodes):
#     msgs = torch.sum(nodes.mailbox['pv'], dim=1)
#     pv = 0.5*(nodes.data['pv'] + msgs)
#     return {'pv' : pv}

# Personalized Page Rank
def pagerank_message_func(edges):
    return {'pv' : edges.src['pv'] / edges.src['deg']}

def pagerank_reduce_func(nodes):
    msgs = torch.sum(nodes.mailbox['pv'], dim=1)
    pv = (1-ALPHA)*msgs + ALPHA*nodes.data['e']
    return {'pv' : pv}

g.register_message_func(pagerank_message_func)
g.register_reduce_func(pagerank_reduce_func)

def pagerank_naive(g):
    # Phase #1: send out messages along all edges.
    for u, v in zip(*g.edges()):
        g.send((u, v))
    # Phase #2: receive messages to compute new PageRank values.
    for v in g.nodes():
        g.recv(v)

def plot_for_offset(g, step):
    fig, ax = plt.subplots(figsize=(10,5))
    pos=nx.spring_layout(g.to_networkx(), seed=SEED)
    colors = g.ndata['pv']
    nc = nx.draw_networkx_nodes(g.to_networkx(), pos,
     node_size=g.ndata['pv']*6000, node_color=g.ndata['pv'], 
     cmap=plt.cm.YlGn, vmax=1., vmin=0., ax=ax)
    plt.colorbar(nc)
    labels = {}
    for node, pv in zip(g.to_networkx().nodes(), g.ndata['pv']):
        labels[node] = "{}:{:.3f}".format(node, pv)
    lc = nx.draw_networkx_labels(g.to_networkx(), pos,
    labels=labels, font_size=5, ax=ax)
    ec = nx.draw_networkx_edges(g.to_networkx(), pos,
    arrows=False, aplha=0.2, ax=ax)
    ax.set_title("Step: {}".format(step))

    # Used to return the plot as an image rray
    fig.canvas.draw()
    image = np.frombuffer(fig.canvas.tostring_rgb(), dtype='uint8')
    image  = image.reshape(fig.canvas.get_width_height()[::-1] + (3,))
    return image

frames = []
for k in range(K):
    print(g.ndata['pv'])
    frames.append(plot_for_offset(g, k))
    imageio.mimsave(
        './ppagerank.gif',
        frames, 
        fps=1)
    pagerank_naive(g)

