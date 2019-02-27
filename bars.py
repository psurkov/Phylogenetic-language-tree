import wikipediaapi
wiki = wikipediaapi.Wikipedia("en")
s1=open('btitles.txt', encoding='utf-8').read().splitlines()
out = open("etitles.txt", "w", encoding='utf-8')
a=set()
s2=[]
for i in s1:
    a.add(i)
def pars(page):
    global s
    global a
    global wiki
    l=page.links
    for title in sorted(l.keys()):
        if wiki.page(str(title)).exists():
            if title not in a:
                s.append(str(title))
                a.add(str(title))
while len(s1)>0:
    s=[s1[-1]]
    s1.pop()
    k=0
    while len(s)<5:
        #можно не 5,а другое минимальное кол-во статей
        pars(wiki.page(s[k]))
        k+=1
    for i in s:
        s2.append(i)
for i in s2:
    out.write(i)
    print(i)
out.close()
    
