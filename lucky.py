n=int(input())
l=[int(i) for i in input().split()]
p=[]
for i in range(len(l)):
	if n*(i+1) in l:
		p.append(l[i])
print(len(p))
