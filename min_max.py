n=int(input())
l=[int(i) for i in input().split()]
m1=min(l)
m2=max(l)
x=[]
for i in range(len(l)):
	if l[i]==m1:
		x.append(i+1)
for i in range(len(l)):
	if l[i]==m2:
		x.append(i+1)
print(*x)
