n,m=map(int,input().split())

but=0
while n!=m:
    but+=1
    if m<n or m%2==1:
        m+=1
    else:
        m=m//2
print(but)