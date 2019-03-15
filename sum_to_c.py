n=int(input())
a=[int(i) for i in input().split()]
b=[int(i) for i in input().split()]
c=[]
for i in range(n):
	c.append(a[i]+b[i])
print(*c)
