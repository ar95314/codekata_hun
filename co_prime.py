m,n=map(int,input().split())
c=0
x=min(m,n)
for i in range(1,x):
    if m%i==0 and n%i==0:
        c=c+1
if c==1:
    print("yes")
else:
    print("no")
