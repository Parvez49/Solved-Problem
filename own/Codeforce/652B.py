

n=int(input())
a=list(map(int,input().split()))

for i in range(n):
    t = a
    for j in range(1,n):
        if j%2==1:
            if a[j]<a[j-1]:
                a[j],a[j-1]=a[j-1],a[j]
        else:
            if a[j]>a[j-1]:
                a[j], a[j - 1] = a[j - 1], a[j]

p=0
for p in range(1,n):
    if p%2==1 and a[p]<a[p-1]:
        break
    elif p%2==0 and a[p]>a[p-1]:
        break


if p==n-1:
    for s in a:
        print(s,end=" ")
else:
    print("Impossible")



