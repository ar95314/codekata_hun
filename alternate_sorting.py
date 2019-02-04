n=int(input())
l=[int(i) for i in input().split()]
x=sorted(l)
y=[]
for i in range(len(x)-1,-1,-1):
    y.append(x[i])
z=[]
for k in range(len(l)):
	if k%2==0:
		z.append(y[0])
		y.remove(y[0])
	else:
		z.append(x[0])
		x.remove(x[0])
	
print(*z)
