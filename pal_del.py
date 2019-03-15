s=input()
t=s[::-1]
if s==t:
	r="YES"
else:
	for i in range(len(s)):
		x=s[:i]+s[i+1:]
		y=x[::-1]
		if x==y:
			r="YES"
			break
		else:
			r="NO"
print(r)
