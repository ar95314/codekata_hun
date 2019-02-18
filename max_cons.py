s=input()
x=""
l=len(s)-1
c,i=1,0
lis=[]
d={}
while i<=l:
	if i<l:
		if s[i]==s[i+1]:
			c+=1
			x+=s[i]
		else:
			if c!=1:
				x+=s[i]
				d.update({x:c})
				lis.append(c)
				x=""
				c=1
	elif i==l:
		if c!=1:
			x+=s[i]
			d.update({x:c})
			lis.append(c)
	i=i+1
m=max(lis)
for k,v in d.items():
	if v==m:
		print(k[0],v)
