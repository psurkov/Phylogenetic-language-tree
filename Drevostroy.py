from ete3 import Tree, TreeStyle
from math import sqrt

f = open('WikiData.txt', 'r')
s = []
tree = Tree()
name2node = {}
for i in f:
    a = ''
    k = 0
    b = []
    while str(i[k]) != ' ':
        a += str(i[k])
        k += 1
    name2node[a] = tree.add_child(name = a)
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
    r = []
    print(s)
    for i in s:
        b = [i[0]]
        for h in s:
            k = 1
            summ = 0
            while k < len(i):
                summ += ((i[k] - h[k]) * (i[k] - h[k]))
                k += 1
            b.append((summ))
        r.append(b)
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
    a = ['(' + r[tx][0] + '+' + r[ty][0] + ')']
    
    while q < len(s[tx]):
        a.append((s[tx][q] + s[ty][q]) / 2)
        q += 1
    s.append(a)
    
    new_name = a[0]
    print(a[0])
    new_node = tree.add_child(name = new_name)
    name2node[new_name] = new_node
    name2node[r[tx][0]].detach()
    name2node[r[ty][0]].detach()
    new_node.add_child(name2node[r[tx][0]], dist = t)
    new_node.add_child(name2node[r[ty][0]], dist = t)
    
    s.pop(tx)
    s.pop(ty - 1)
while len(s) > 1:
    rang()
#edge_labels=networkx.draw_networkx_edge_labels(g,pos=networkx.spring_layout(g),edge_labels=None,label_pos=1,clip_on=True)
def pavuk():
	tree.show()
pavuk()
