n=int(input())
l=[int(i) for i in input().split()]
d={}
lis=[]
for i in l:
    x=l.count(i)
    lis.append(x)
    d.update({i:x})
m=max(lis)
for x,y in d.items():
    if y==m:
        print(x)
