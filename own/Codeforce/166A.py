

n,k=map(int,input().split())
a=list()
for i in range(n):
    t=list(map(int,input().split()))
    a.append(t)

a.sort(key=lambda x:(x[0],-x[1]),reverse=True)
#print(len(a))
#print(a)
cou=a.count(a[k-1])
print(cou)