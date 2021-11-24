


n,m=map(int,input().split())


if n>m*2:
    mi=n-m*2
else:mi=0

for i in range(n):
    comEdge = i * (i - 1) / 2
    ma=0
    #print(comEdge)
    if comEdge>=m:
        #print(n,i)
        ma=abs(n-(i))
        break
print(mi,ma)






