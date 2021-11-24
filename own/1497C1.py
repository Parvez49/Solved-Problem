import math

for _ in range(int(input())):
    n, k = map(int, input().split())
    if n%4==0:
        print(math.floor(n/4),math.floor(n/4),int(n/2))
    elif n%2==0:
        print(math.floor((n - 2) / 2), math.floor((n - 2) / 2), 2)
    else:
        print(math.floor(n / 2), math.floor(n / 2), 1)

