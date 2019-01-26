n=int(input())
l=[int(i) for i in input().split()]
y=[[l[i],l[j]] for i in range(len(l)) for j in range(len(l)) if i<j if (l[i]+l[j])==0]
for g in y:
    for h in range(0,len(g)):
        if h==0:
            print(g[h],end="")
        else:
            print("",g[h],end="")
    if len(y)>1:
        print()
