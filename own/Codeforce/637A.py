
n=int(input())
a=list(map(int,input().split()))

id=list()
ind=list()
like=list()

for i in range(n):
    if a[i] not in id:
        id.append(a[i])
        ind.append(i)
        like.append(1)
    else:
        ii=id.index(a[i])
        like[ii]+=1
        ind[ii]=i

lind=like.index(max(like))

iid=id[lind]
maxlik=like[lind]
iind=ind[lind]

like.remove(like[lind])
ind.remove(ind[lind])
id.remove(id[lind])

while(1):
    if maxlik not in like:
        print(iid)
        exit()
    else:

        ti=like.index(max(like))
        if like[ti]!=maxlik:
            break
        else:
            if ind[ti]<iind:
                iind=ind[ti]
                iid=id[ti]
            else:
                lind=ti
            like.remove(like[lind])
            ind.remove(ind[lind])
            id.remove(id[lind])


