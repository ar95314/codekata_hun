n=int(input())
x=""
l=[int(i) for i in input().split()]
l1=l[::-1]
for i in range(len(l1)):
	if i!=len(l1)-1:
		x+=str(l1[i])+"->"
	else:
		x+=str(l1[i])
print(x)
"""n=int(input())
x=""
l=[i for i in input().split()]
l1=l[::-1]
for i in range(len(l1)):
	if i!=len(l1)-1:
		x+=l1[i]+"->"
	else:
		x+=l1[i]
print(x)"""
