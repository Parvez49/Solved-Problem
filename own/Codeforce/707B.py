

n,m,k=map(int,input().split())
inf=1000000001
gr=list()
#print(3,gr[n-1])
for i in range(m):
    u,v,l=map(int,input().split())
    gr.append([u,v,l])
#print(gr)
s=set()
if k:
    s=set(map(int,input().split()))
#print(s)
res=list()
for u,v,w in gr:
    #print(u,v,w)
    if (u in s)^(v in s):
        res.append(w)
#print(res)
print(min(res) if res else -1)






