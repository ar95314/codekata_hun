def prod(l):
	p=1
	for i in l:
		p*=i
	return p
n=int(input())
lis=[int(i) for i in input().split()]
x=[]
for i in lis:
	y=lis[0]
	lis.remove(y)
	x.append(prod(lis))
	lis.append(y)
print(*x)
