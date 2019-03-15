n=int(input())
l1=[int(i) for i in input().split()]
l2=[int(i) for i in input().split()]
c=0
while l1!=l2:
	x=l1[0]
	l1.append(x)
	l1.remove(x)
	c+=1
print(c)
