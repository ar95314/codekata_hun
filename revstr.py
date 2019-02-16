l=[i for i in input().split()]
x=[]
for i in l:
    x.append(i[::-1])
print(*x)
