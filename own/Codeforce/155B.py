n = int(input())

li = list()
for i in range(n):
    a = list(map(int, input().split()))
    li.append(a)
li.sort(key=lambda x: (x[1], x[0]), reverse=True)

# print(li)
k = 0
c = 1
a = 0
while (1):
    c -= 1
    a += li[k][0]
    c += li[k][1]
    if c == 0 or k == n - 1:
        break
    k += 1

print(a)