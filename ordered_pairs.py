n=int(input())
l=[int(i) for i in input().split()]
x=[[l[i],l[j]] for i in range(len(l)) for j in range(len(l)) if i<j and l[i]<l[j]]
print(len(x))
