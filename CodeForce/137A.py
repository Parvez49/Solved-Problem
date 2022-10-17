import math

for _ in range(int(input())):
    n=int(input())
    input()
    print(int((math.perm(4,2)*math.comb(10-n,2))/2))
