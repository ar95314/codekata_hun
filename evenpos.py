def evenpos(l):
	x=[]
	for i in range(len(l)):
		if (i+1)%2==0:
			x.append(l[i])
	return x
n=int(input())
lis=[int(i) for i in input().split()]
y=lis
i=1
while i!=len(y):
	if len(y)>1:
		y=evenpos(y)
for i in range(len(lis)):
	if lis[i]==y[0]:
		print(i)
