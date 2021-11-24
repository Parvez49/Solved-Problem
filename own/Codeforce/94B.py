



m=int(input())
fr=[0]*(5)

for i in range(m):
    u,v=map(int,input().split())
    fr[u-1]+=1
    fr[v-1]+=1
#print(fr)

if max(fr)==min(fr)==2:print("FAIL")
else:print("WIN")


