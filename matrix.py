n=int(input())
arr=[]
for i in range(0,n):
    for j in range(0,n):
       arr[i][j]=input()
print(arr)
x=[]
for i in range(n):
	for j in range(n):
		if i==j:
			x.append(arr[i][j])
print(x)
print(sum(x))
