

n,q=map(int,input().split())
a=list(map(int,input().split()))
t=list(map(int,input().split()))

ans=list()
temp=list()
index=list()
#print(len(temp))
for i in t:
    if i in temp:
        ans.append(temp.index(i)+1)
    else:
        ind=a.index(i)
        c=0
        for j in index:
            if j<ind:
                c+=1


        ans.append(len(temp)+a.index(i)-c+1)
        temp.insert(0, i)
        index.append(ind)
        #print(temp)
print(temp)
print(index)
for i in ans:
    print(i,end=" ")
