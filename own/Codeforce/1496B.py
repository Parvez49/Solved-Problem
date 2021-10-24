import math

for t in range(int(input())):

    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    #print(a)
    a.sort()
    me=-1
    ma = a[n - 1]
    #print("ph")
    for j in range(n):
        if j != a[j]:
            me=j
            break
    if me==-1: me=n
    b=math.ceil((me+ma)/2)
    if me==n or k==0:
        print(len(a)+k)
    else:
        if b not in a:
            print(len(a)+1)
        else:
            print(len(a))