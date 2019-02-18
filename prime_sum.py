def isprime(n):
	for i in range(2,n):
		if n%i==0:
			return 0
			break
	else:
		return 1
n=int(input())
x=[[i,j] for i in range(2,n) for j in range(2,n) if isprime(i)==1 and isprime(j)==1 and (i+j)==n]
print(*x[0])
