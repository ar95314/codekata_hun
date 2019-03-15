n=int(input())
x,y=[],[]
l=[int(i) for i in input().split()]
for i in range(len(l)):
	if i==len(l)-1:
		x.append(0)
	else:
		y=l[i+1:]
		x.append(max(y))
print(*x)
