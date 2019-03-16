n,k=map(int,input().split())
x=[int(i) for i in input().split()]
while k in x:
	x.remove(k)
if len(x)!=0:
	print(*x)
else:
	print("empty")
