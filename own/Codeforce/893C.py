

n,m=map(int,input().split())
gold=[0]+list(map(int,input().split()))


ck=[i for i in range(n+1)]

def find(a):
    while(ck[a]!=a):
        ck[a]=ck[ck[a]]
        a=ck[a]
    return a


for j in range(m):
    u,v=map(int,input().split())
    u=find(u)
    v=find(v)
    if gold[u]<gold[v]:
        ck[v]=u
    else:ck[u]=v

print(sum(gold[i] for i in range(n+1) if ck[i]==i))










