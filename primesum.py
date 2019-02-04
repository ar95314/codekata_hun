#ice
def isprime(x):
    c=1
    for i in range(2,x):
        if x%i==0:
            c=0
            break
    return c
n=int(input())
l=[]
d=0
for i in range(2,n):
    if isprime(i)==1:
        l.append(i)
l1=l
for i in l:
    for j in l1:
        if (i+j)==n:
            l1.remove(j)
            d+=1
print(d)
