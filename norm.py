d = open('data1.txt', encoding='utf-8').read().splitlines()
out = open('data2.txt', 'w')
for s in d:
	l = s.split()[1:-1]
	l = [int(i) for i in l]
	ls = sorted(l)
	m = ls[len(ls) // 2]
	if m > 0:
		l = [i / m for i in l]
	out.write(s.split()[0] + ' ' + ' '.join([str(i) for i in l]) + '\n')
