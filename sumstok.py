n,k=map(int,input().split())
l=[int(i) for i in input().split()]
x=[l[i]+l[j] for i in range(len(l)) for j in range(len(l)) if (l[i]+l[j])==k and i!=j]
if len(x)!=0:
	print("YES")
else:
	print("NO")
