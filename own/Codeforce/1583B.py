for t in range(int(input())):
    n,m=map(int,input().split())
    tree=[1]*n
    for i in range(m):
        a,b,c=map(int,input().split())
        tree[b-1]=0

    i=tree.index(1)
    for p in range(1,n+1):
        if p!=i+1:
            print(i+1,p)
