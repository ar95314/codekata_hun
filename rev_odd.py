s=input().split()
x=[]
for i in range(len(s)):
	if (i+1)%2==1:
		x.append(s[i][::-1])
	else:
		x.append(s[i])
print(*x)
