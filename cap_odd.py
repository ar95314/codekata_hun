x=input()
d=""
j=0
c=0
for i in range(len(x)):
    if x[i]!=" ":
        j+=1
        if j%2==1:
            d+=x[i].upper()
        else:
            d+=x[i]
    else:
        d+=x[i]
print(d)
