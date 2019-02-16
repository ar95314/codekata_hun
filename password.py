s,t=map(str,input().split())
l,k=list(s),list(t)
x=abs(len(l)-len(k))
for i in range(1,x+1):
    if len(l)>len(k):
        k.append(i)
    else:
        l.append(i)
z=[]
for i in range(len(l)+len(k)):
    if i%2==0:
        z.append(l[0])
        l.remove(l[0])
    else:
        z.append(k[0])
        k.remove(k[0])
for i in z:
    print(i,end="")
