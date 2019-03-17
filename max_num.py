n=int(input())
l=[int(i) for i in input().split()]
s=""
x=sorted(l,reverse=True)
for i in x:
	if x.count(i)==len(x) and i==0:
		print(0)
		break
	else:
		s+=str(i)
print(s)
