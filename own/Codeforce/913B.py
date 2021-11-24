
n=int(input())
tree=[[] for i in range(n)]
edge=[0]*n
nonleaf=list()

for i in range(n-1):
    a=int(input())
    tree[a-1].append(i+2)
    edge[a-1]+=1
#print(tree)

for i in range(n):
    if len(tree[i])!=0:
        nonleaf.append(i+1)
#print(nonleaf)
for j in range(len(nonleaf)):
    c=0
    for k in tree[nonleaf[j]-1]:
        if k not in nonleaf:
            c+=1
    if c<3:
        print("No")
        exit()

print("Yes")


