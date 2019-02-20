l=input()
if len(l)%2==1:
	i=len(l)//2
	x=l[:i]
	y=l[i+1:]
	if x==y:
		print("YES")
else:
	print("NO")
