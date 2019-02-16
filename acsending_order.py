n=int(input())
l=[i for i in input().split()]
x=[]
for i in l:
    x.append(i.lower())
k=sorted(x)
for i in k:
    print(i)
