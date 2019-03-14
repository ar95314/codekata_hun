def dig(x):
	c=0
	x=str(x)
	for i in x:
		c+=int(i)
	return c
n=int(input())
for i in range(1,100000000000):
	if dig(i)==n:
		print(i)
		break
