

n,x=map(int,input().split())
a=list(map(int,input().split()))

a.sort()

op=0
c=0

t=list()
for j in range(x):
    t.append(j)


if x in a:
    op+=1
for i in range(max(n,x)):
    if i==min(n,x):
        break
    if t[i] not in a:

        op+=1

if x>n:

    for p in range(i,x):
        if t[p] not in a:
            op+=1


print(op)






