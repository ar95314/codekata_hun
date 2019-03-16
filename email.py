s=input()
c,f=0,0
if s.count('@')==1 and s.count('.')==1 and s[-4:]==".com":
	for i in range(len(s)):
		if s[i]=='@':
			f=1
			if len(s[:i])>=3:
				c+=1
			else:
				p="NO"
				break
		elif s[i]==".":
			if c>=4:
				p="YES"
			else:
				p="NO"
				break
		elif f==1:
			c+=1
else:
	p="NO"
print(p)
