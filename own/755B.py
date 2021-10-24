

n,m=map(int,input().split())

pb=list()
eb=list()
for i in range(n):
    pb.append(input())
com=0
for j in range(m):
    eb.append(input())
    if eb[j] in pb:
        com+=1
if com%2==1:
    if n>m-1:
        print("YES")
    else: print("NO")
else:
    if n>m:
        print("YES")
    else: print("NO")

