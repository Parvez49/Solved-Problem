import math
for t in range(int(input())):
    L,v,l,r=map(int,input().split())
    a=math.ceil(l/v)*v
    b=math.floor(r/v)*v
    #print(a,b)
    if a<=b:
        m=(b-a)/v+1
        print(int(int(L / v) - ((b-a)/v+1)))
    else:
        print(int(L/v))