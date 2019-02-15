def bin_count(x):
	b=bin(x)
	y=b[2:]
	c=y.count('1')
	return c
def prime(n):
	x1=0
	if n!=1:
		for i in range(2,n):
			if n%i==0:
				return 0
				break
		else:
			return 1
a,b=map(int,input().split())
k=0
for i in range(a,b+1):
	x=bin_count(i)
	if prime(x)==1:
		k+=1
print(k)
