
n,k=map(int,input().split())
st=list(input())
k=list(input())
c=0
ans=0
for i in range(n):
    if st[i] in k:
        c+=1
    else:
        ans+=((c+1)*c)/2
        c=0
ans+=((c+1)*c)/2
print(int(ans))