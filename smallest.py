n=int(input())
x=[int(i) for i in input().split()]
z=[]
for i in range(len(x)):
	y=x[:i+1]
	z.append(min(y))
print(*z)
