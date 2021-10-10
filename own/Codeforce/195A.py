import math

a,b,c=map(int,input().split())

for i in range(1,math.ceil(a*c/b)):
    if (a*c-b*i)<=c*b:
        break
print(i)