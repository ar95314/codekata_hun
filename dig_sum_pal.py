n=input()
s=0
for i in n:
	s+=int(i)
p=str(s)
if p==p[::-1]:
	print("YES")
else:
	print("NO")
