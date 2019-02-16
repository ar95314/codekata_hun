def prime(n):
    for j in range(2,n):
        if n%j==0:
            return 0
            break
    else:
        return 1
n=int(input())
l=[]
for i in range(2,n):
    if prime(i)==1:
        l.append(i)
if len(l)==0:
    print('0')
else:
    print(*l)
