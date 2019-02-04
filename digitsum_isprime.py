def isprime(x):
    c=0
    if x==1:
        return c
    for i in range(2,x):
        if x%i==0:
            c=0
            break
    else:
        c=1
    return c
def digsum(x):
    a,b=0,0
    while x!=0:
        a=x%10
        b=b+a
        x=x//10
    return b
l,r=map(int,input().split())
lis=[i for i in range(l,r+1) if isprime(digsum(i))==1]
print(len(lis))
