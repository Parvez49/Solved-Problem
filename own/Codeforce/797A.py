import math

n, k = map(int, input().split())
a = list()
c, k = 0, k - 1
tk = k
while (k):
    b = 0
    for j in range(2, math.floor(n / 2) + 1):
        if n % j == 0:
            b = 1
            n = int(n / j)
            a.append(j)
            c += 1
            break

    k -= 1
    if b == 0: break
    if k == 0:
        a.append(n)
        c += 1

if tk == 0:
    print(n)
elif c == tk + 1:
    for i in a:
        print(i, end=" ")
else:
    print(-1)