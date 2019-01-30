n,m=map(int,input().split())
s=[i for i in input().split()]
t=[i for i in input().split()]
c=0
if len(t)>len(s):
	print("NO")
else:
	for k in t:
		if k in s:
			c=c+1
	if c==len(t):
		print("YES")
	else:
		print("NO") 
 
