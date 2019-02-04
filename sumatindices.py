n=int(input())
l=[int(i) for i in input().split()]
c=0
for i in range(1,len(l)):
    l1=[l[x] for x in range(0,i)]
    l2=[l[y] for y in range(i+1,len(l))]
    if sum(l1)==sum(l2):
        c=c+1
        break
if c==1:
    print("yes")
else:
    print("no")
