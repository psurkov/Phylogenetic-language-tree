import networkx
import matplotlib.pyplot as plt
from Bio import Phylo
from Bio.Phylo.TreeConstruction import *
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor

def vec_dist(a, b):
    dst = 0
    for i in range(len(a)):
        dst += (a[i] - b[i]) ** 2
    dst = dst ** 0.5
    return dst

f = open('data2.txt', 'r')
names = []
vecs = []
for line in f:
    names.append(line.split()[0])
    vecs.append([float(i) for i in line.split()[1:-1]])


dist = [[0] * (i + 1) for i in range(len(vecs))]
for i in range(len(vecs)):
    for j in range(i + 1):
        dist[i][j] = (vec_dist(vecs[i], vecs[j]))
print(dist)
dm = DistanceMatrix(names = names, matrix = dist)
constructor = DistanceTreeConstructor()
tree = constructor.upgma(dm)
for i in tree.find_clades({"name": "Inner.*"}):
	i.name = ""
Phylo.draw(tree, branch_labels=lambda c: str(round(c.branch_length, 2)))
