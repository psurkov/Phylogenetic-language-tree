import numpy as np
import matplotlib.pyplot
from sklearn.decomposition import PCA

lines = open('data2.txt', 'r').read().splitlines()
names = []
X = np.zeros((len(lines), len(lines[0].split()) - 1))
for i, line in enumerate(lines):
    names.append(line.split()[0])
    l = line.split()[1:-1]
    for j in range(len(l)):
        X[i][j] = float(l[j])

pca = PCA(n_components=2)
Y = pca.fit_transform(X)

matplotlib.pyplot.scatter(Y[:,0], Y[:,1])
for label, x, y in zip(names, Y[:,0], Y[:,1]):
    matplotlib.pyplot.annotate( label, xy=(x, y), xytext=(-2, 2), textcoords='offset points', ha='right', va='bottom' )
matplotlib.pyplot.axis('scaled')
matplotlib.pyplot.show()
