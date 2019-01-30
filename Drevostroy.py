import networkx
import matplotlib.pyplot as plt
from math import sqrt

g = networkx.Graph()
f = open('wikiData.txt','r')
s = []
for i in f:
    a = ''
    k = 0
    b = []
    print(i[k])
    while str(i[k]) != ' ':
        a += str(i[k])
        print(a)
        k += 1
    b.append(a)
    while k < len(i) - 1:
        c = ''
        while str(i[k]) != ' ' and k < len(i) - 1:
            c += str(i[k])
            k += 1
        if c != '':
            b.append(int(c))
        if str(i[k]) == ' ':
            k += 1
    s.append(b)
def rang():
    global s
    global g
    r = []
    for i in s:
        b = [i[0]]
        for h in s:    
            k = 1
            summ = 0
            while k<len(i):
                summ += ((i[k] - h[k]) * (i[k] - h[k]))
                k += 1
            b.append((summ))
        r.append(b)
    for i in r:
        print(i)
    print('_________')
    y = 0
    ty = 0
    tx = 2
    t = r[ty][tx]
    for y, line in enumerate(r):
        for x, dot in enumerate(line):
            if x !=0 and dot !=0 and dot <= t:
                t = dot
                tx = x - 1
                ty = y
    q = 1
    a = ['(' + r[tx][0] + '+' +r[ty][0] + ')']
    while q < len(s[tx]):
        a.append((s[tx][q] + s[ty][q]) / 2)
        q += 1
    s.append(a)
    g.add_nodes_from([r[tx][0], r[ty][0], s[-1][0]])
    g.add_edges_from([(r[ty][0], s[-1][0],{'weight':t / 2}),(r[tx][0],s[-1][0], {'weight':t / 2})])
    s.pop(tx)
    s.pop(ty - 1)
    for i in s:
        print(i)
    print('_________')
while len(s) > 1:
    rang()
#edge_labels=networkx.draw_networkx_edge_labels(g,pos=networkx.spring_layout(g),edge_labels=None,label_pos=1,clip_on=True)
def pavuk():
    networkx.draw(g)
    networkx.draw_networkx_labels(g, pos = networkx.spring_layout(g))
    plt.show()
pavuk()
