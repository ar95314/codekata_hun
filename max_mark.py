def mark(l):
	m=l[1:]
	c=0
	for i in m:
		c+=int(i)
	return(c)
s1=input().split('#')
s2=input().split('#')
if mark(s1)>mark(s2):
	print(s1[0])
else:
	print(s2[0])
