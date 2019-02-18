r=int(input())
c=0
n=str(2)
for i in range(1,r+1):
	x=str(i)
	y=x.count(n)
	if str(n) in str(i):
		c+=y
print(c)
