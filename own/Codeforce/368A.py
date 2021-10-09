

n,d=map(int,input().split())
a=list(map(int,input().split()))
m=int(input())

a.sort()
ben=0
los=0

if n>m:
    print(sum(a[:m]))
else:
    if n==m:
        print(sum(a))
    else:
        print(sum(a)-d*(m-n))
