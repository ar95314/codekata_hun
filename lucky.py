n=int(input())
l=[int(i) for i in input().split()]
for i in range(len(l)):
	if n*(i+1) in l:
		p=l[i]
		break
	else:
		p=0
print(p)
