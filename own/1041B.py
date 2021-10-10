import math

a,b,x,y=map(int,input().split())

gcd=math.gcd(x,y)
x/=gcd
y/=gcd
print(min(int(a/x),int(b/y)))