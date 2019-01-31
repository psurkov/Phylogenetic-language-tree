from ete3 import Tree, TreeStyle
from math import sqrt

f = open('data2.txt', 'r')
s = []
tree = Tree()
name2node = {}
for line in f:
    lang = line.split()[0]
    name2node[lang] = tree.add_child(name = lang)
    s.append([lang] + [float(i) for i in line.split()[1:-1]])
    
def lang_dist(a, b):
    dst = 0
    for i in range(1, len(a)):
        dst += (a[i] - b[i]) ** 2
    dst = dst ** 0.5
    return dst

def lang_abs(a):
    dst = 0
    for i in range(1, len(a)):
        dst += a[i] ** 2
    dst = dst ** 0.5
    return dst
    
def rang():
    global s
    x, y, best_dist = 0, 1, lang_dist(s[0], s[1])
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            d = lang_dist(s[i], s[j])
            if d < best_dist:
                x = i
                y = j
                best_dist = d
            print(s[i][0], s[j][0], d)
    
    a = ['(' + s[x][0] + '+' + s[y][0] + ')']
    wx = s[x][0].count('+') + 1
    wy = s[y][0].count('+') + 1
    for i in range(1, len(s[x])):
        a.append((s[x][i] * wx + s[y][i] * wy) / (wx + wy))
    
    new_name = a[0]
    new_node = tree.add_child(name = new_name)
    name2node[new_name] = new_node
    name2node[s[x][0]].detach()
    name2node[s[y][0]].detach()
    new_node.add_child(name2node[s[x][0]], dist = best_dist)
    new_node.add_child(name2node[s[y][0]], dist = best_dist)
    
    s.pop(x)
    s.pop(y - 1)
    s.append(a)
    
while len(s) > 1:
    rang()

tree.show()
