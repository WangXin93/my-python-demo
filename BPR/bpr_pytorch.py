import numpy
import os
import random
from collections import defaultdict
import torch
import torch.nn as nn
import torch.optim as optim
from tqdm import trange


def load_data(data_path):
    user_ratings = defaultdict(set)
    max_u_id = -1
    max_i_id = -1
    with open(data_path, 'r') as f:
        for line in f.readlines():
            u, i, _, _ = line.split("\t")
            u = int(u)
            i = int(i)
            user_ratings[u].add(i)
            max_u_id = max(u, max_u_id)
            max_i_id = max(i, max_i_id)
    print ("max_u_id:", max_u_id)
    print ("max_i_id:", max_i_id)
    return max_u_id, max_i_id, user_ratings
    

data_path = './ml-100k/u.data'
user_count, item_count, user_ratings = load_data(data_path)

def generate_test(user_ratings):
    user_test = dict()
    for u, i_list in user_ratings.items():
        user_test[u] = random.sample(user_ratings[u], 1)[0]
    return user_test

user_ratings_test = generate_test(user_ratings)

# 生成若干批训练集
def generate_train_batch(user_ratings, user_ratings_test, item_count, batch_size=512):
    t = []
    for b in range(batch_size):
        u = random.sample(user_ratings.keys(), 1)[0]
        i = random.sample(user_ratings[u], 1)[0]
        while i == user_ratings_test[u]:
            i = random.sample(user_ratings[u], 1)[0]
        
        j = random.randint(1, item_count)
        while j in user_ratings[u]:
            j = random.randint(1, item_count)
        t.append([u, i, j])
    return numpy.asarray(t)

# 生成测试三元组
def generate_test_batch(user_ratings, user_ratings_test, item_count):
    for u in user_ratings.keys():
        t = []
        i = user_ratings_test[u]
        for j in range(1, item_count+1):
            if not (j in user_ratings[u]):
                t.append([u, i, j])
        yield numpy.asarray(t)


class BPR_MF(nn.Module):
    def __init__(self, user_count, item_count, hidden_dim):
        super(BPR_MF, self).__init__()
        self.user_emb_w = nn.Embedding(user_count+1, hidden_dim)
        self.item_emb_w = nn.Embedding(item_count+1, hidden_dim)

        nn.init.normal_(self.user_emb_w.weight, 0, 0.1)
        nn.init.normal_(self.item_emb_w.weight, 0, 0.1)

    def forward(self, u, i, j):

        u_emb = self.user_emb_w(u)
        i_emb = self.item_emb_w(i)
        j_emb = self.item_emb_w(j)

        # MF predict u_i > u_j
        x = torch.sum(torch.mul(u_emb, (i_emb - j_emb)), 1, keepdim=True)

        # AUC for one user:
        mf_auc = torch.mean(torch.gt(x, 0).float())

        l2_norm = torch.sum(u_emb * u_emb) + \
            torch.sum(i_emb * i_emb) + \
            torch.sum(j_emb * j_emb)

        bprloss = 1e-4 * l2_norm - torch.mean(torch.log(torch.sigmoid(x)))
        return mf_auc, bprloss, l2_norm

device = torch.device("cpu")
bpr_mf = BPR_MF(user_count, item_count, 20).to(device)
optimizer = optim.SGD(bpr_mf.parameters(), lr=0.01)

for epoch in range(1, 4):
    _batch_bprloss = 0
    for k in trange(1, 5000):
        uij = generate_train_batch(user_ratings, user_ratings_test, item_count)

        u = torch.from_numpy(uij[:, 0]).to(device)
        i = torch.from_numpy(uij[:, 1]).to(device)
        j = torch.from_numpy(uij[:, 2]).to(device)
        _, _bprloss, _l2_norm = bpr_mf(u, j, j)
        _batch_bprloss += _bprloss.item()

        bpr_mf.zero_grad()
        _bprloss.backward()
        optimizer.step()

    print("Epoch: {}".format(epoch))
    print("bprloss: {}".format(_batch_bprloss / k))
    print("l2_norm: {}".format(_l2_norm*1e-4))

    # Test
    user_count = 0
    _auc_sum = 0.0

    for t_uij in generate_test_batch(user_ratings, user_ratings_test, item_count):
        u = torch.from_numpy(t_uij[:, 0]).to(device)
        i = torch.from_numpy(t_uij[:, 1]).to(device)
        j = torch.from_numpy(t_uij[:, 2]).to(device)

        with torch.no_grad():
            _auc, _test_bprloss, _test_l2_norm = bpr_mf(u, i, j)

        user_count += 1
        _auc_sum += _auc
    print("test_loss {} test_auc: {} test_l2_norm: {}".format(
        _test_bprloss, _auc_sum / user_count, _test_l2_norm*1e-4))
    print()

# Predict
u1_dim = torch.unsqueeze(bpr_mf.user_emb_w.weight[0], 0)
u1_all = torch.matmul(u1_dim, bpr_mf.item_emb_w.weight.transpose(0, 1))
result_1 = u1_all.cpu().data.numpy()
print(result_1)

print("以下是用户0的推荐：")
p = numpy.squeeze(result_1)
p[numpy.argsort(p)[:-5]] = 0
for index in range(len(p)):
    if p[index] != 0:
        print(index, p[index])
