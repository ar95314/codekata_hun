n=int(input())
x=[int(i) for i in input().split()]
y=[]
for i in range(len(x)-1):
	if x[i]>x[i+1]:
		y.append(x[i+1])
	else:
		y.append(-1)
if x[-1]>x[0]:
	y.append(x[i+1])
else:
	y.append(-1)
print(*y)
