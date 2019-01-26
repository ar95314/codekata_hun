n=int(input())
x=[i for i in input().split()]
d=[]
for i in range(0,len(x)):
    if x[i] not in d:
        d.append(x[i])
    else:
        print(x[i])
        break

