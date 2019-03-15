n=int(input())
x=[int(i) for i in input().split()]
m1=min(x)
m2=max(x)
if x.count(x[0])==len(x):
		print(0)
else:
	for i in range(len(x)):
		if x[i]==m1:
			mi1=i
		elif x[i]==m2:
			mi2=i
	if mi1<mi2:
		print(m2-m1)
