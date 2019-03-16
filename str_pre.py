n=int(input())
l=[i for i in input().split()]
k=input()
l1=len(k)
c=0
for i in l:
	if i[:l1]==k:
		c+=1
print(c)
