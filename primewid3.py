def isprime(x):
    c=0
    for i in range(2,x):
        if x%i==0:
            c=0
    else:
        c=1
    return c
n=int(input())
y=0
for i in range(2,n):
    if isprime(i)==1:
        s=str(i)
        if s[-1]=="3":
            y=y+i
print(y)
