n,k=map(int,input().split())
l=[int(i) for i in input().split()]
for i in range(k):
	x=l[0]
	l.remove(l[0])
	l.append(x)
print(*l)
