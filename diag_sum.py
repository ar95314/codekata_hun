n=int(input())
l=[]
x=[]
for i in range(n):
    l.append(input().split())
x=[int(l[i][j]) for i in range(len(l)) for j in range(len(l)) if (i+j)==len(l)-1]
print(sum(x))
