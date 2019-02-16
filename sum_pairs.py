n=int(input())
l=[int(i) for i in input().split()]
x=[[l[i],l[j]] for i in range(len(l)) for j in range(len(l)) for k in range(len(l))  if i<j<k and l[i]+l[j]==l[k]]
print(len(x))
