n=int(input())
l=[]
x=[]
for i in range(n):
    l.append(input().split())
x=[int(l[i][i]) for i in range(len(l))]
print(sum(x))
