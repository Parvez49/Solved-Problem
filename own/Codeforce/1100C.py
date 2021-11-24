import math

n,r=map(int,input().split())

t=math.sin(math.pi/(n))
print(r*t/(1-t))