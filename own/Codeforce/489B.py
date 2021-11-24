

n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
a.sort()
b.sort()
ib=[0]*m
c=0
for i in range(n):
    for j in range(m):
        if ib[j]==0 and (abs(a[i]-b[j])==0 or abs(a[i]-b[j]))==1:
            c+=1
            ib[j]=1
            break
        elif a[i]<b[j] and ib[j]==0 and abs(a[i]-b[j])>1:
            break
print(c)
