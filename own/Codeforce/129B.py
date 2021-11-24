n,m = map(int,input().split())
gr = [set() for i in range(n)]

for i in range(m):
    u,v=map(int,input().split())
    gr[u-1].add(v-1)
    gr[v-1].add(u-1)
group=0
while(1):
    repim=set()
    for i in range(n):
        if len(gr[i])==1:
            repim.add(i)
            gr[i]=set()
    if len(repim)==0:
        break
    group+=1
    for i in range(n):
        gr[i]=gr[i]-repim
print(group)

