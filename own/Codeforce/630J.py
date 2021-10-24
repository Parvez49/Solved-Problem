import math

n=int(input())

def lcm(a,b):
    res=a
    for i in range(a+1,b+1):
        res=int((res*i)/math.gcd(res,i))
    return res
print(int(n/lcm(2,10)))