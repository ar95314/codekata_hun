n=int(input())
l=[]
for i in range(n,0,-1):
    x='1'*i
    l.append(x)
for i in l:
    if len(l)!=1:
        for j in i:
            print(i[-1],end=" ")
            i=i[:-1]
    else:
        print(i)
        break
    print()
