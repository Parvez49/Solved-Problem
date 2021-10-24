

for t in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    e,o,f=0,0,0
    a.sort()
    for i in range(1,n):
        if a[i]%2==0:
            e+=1
        else:
            o+=1
        if a[i]-a[i-1]==1:
            f+=1
    if (a[0]%2==0):
        e+=1
    else: o+=1

    if e%2==0 and o%2==0:
        print("yes")
    elif e%2==1 and e%2==1:
        if f>=1: print("yes")
        else: print("no")
    elif o!=e: print("no")
    else: print("no")