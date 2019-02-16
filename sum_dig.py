n=input()
i=0
y=[]
j=len(n)
for _ in range(i,j):
    x=n[i:j]
    for k in x:
        y.append(int(k))
    j-=1
print(sum(y))
