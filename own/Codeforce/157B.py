import math

n=int(input())
a=list(map(int,input().split()))

a.sort(reverse=True)
area=0
pi=3.1416
if n==1:
    print(pi*a[0]*a[0])
else:
    if n%2==0:
        for i in range(n-1,0,-2):
            area+=(pi*a[i]*a[i]-pi*a[i-1]*a[i-1])
    else:
        for j in range(n-1,1,-2):
            area += (pi * a[j] * a[j] - pi * a[j - 1] * a[j - 1])
        area+=pi*a[0]*a[0]
    print(abs(area))
