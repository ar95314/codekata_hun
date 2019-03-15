a,b=map(int,input().split())
c=0
if b>a:
	print(0)
else:
	x=a-b
	c+=1
	while x>0:
		x=x-b
		c+=1
	if x==0:
		print(c)
