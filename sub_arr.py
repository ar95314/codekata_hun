s=input()
t=input()
if t in s:
	for i in range(len(s)):
		if s[i]==t[0]:
			print(i)
			break
else:
	print(-1)
