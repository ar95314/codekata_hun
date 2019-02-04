a=input()
b=input()
x=[]
c=list(b)
for i in range(len(a)):
	for j in range(len(b)):
		if a[i]==c[j]:
			x.append(a[i])
			c.remove(b[j])
print(x)
