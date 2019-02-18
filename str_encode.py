s=input()
x=""
l=len(s)-1
c,i=1,0
while i<=l:
	if i<l:
		if s[i]==s[i+1]:
			c+=1
		else:
			if c!=1:
				x+=str(c)+"*"+s[i]
				c=1
			else:
				x+=s[i]
				c=1
	elif i==l:
		if c!=1:
			x+=str(c)+"*"+s[i]
		else:
			x+=s[i]
	i=i+1
print(x)
