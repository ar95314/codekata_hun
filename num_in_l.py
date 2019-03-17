n,k=map(int,input().split())
x,y=[],[]
c=0
for i in range(n):
	l=[int(i) for i in input().split()]
	x.append(l)
for i in l:
	for j in x:
		if i in j:
			c+=1
	if c==len(x) and i not in y:
		y.append(i)
		c=0
	else:
		c=0
print(*y)
