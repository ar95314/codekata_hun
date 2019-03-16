def prime(n):
	r=0
	if n==2:
		r=1
	else:
		for i in range(2,n):
			if n%i==0:
				r=0
				break
			else:
				r=1
	return r
n=int(input())
x=[]
for i in range(2,n):
	if prime(i)==1:
		x.append(i)
y=[[x[i],x[j],x[k]] for i in range(len(x)) for j in range(len(x)) for k in range(len(x)) if x[i]+x[j]+x[k]==n]
print(*y[0])
