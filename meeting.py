n,k=map(int,input().split())
x=[int(i) for i in input().split()]
c=0
for i in x:
	if i<=k:
		c+=1
print(c)
