n,k=map(int,input().split())
x,s=[],[]
d=0
for i in range(n):
	x.append(input().split())
l=x[0]

for i in range(1,len(x)):
	c=0
	for j in l:
		if j in x[i]:
			s.append(j)
			c=1
		if c==1:
			d+=1
	print(d)
if d==n:
	print(s)
