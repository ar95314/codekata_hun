n=int(input())
l=[int(i) for i in input().split()]
h=[]
for x in range(0,len(l)):
    if x==l[x]:
        h.append(l[x])
if len(h)==0:
    print("-1")
else:
    for j in range(len(h)):
        if j==0:
            print(h[j],end="")
        else:
            print("",h[j],end="")
