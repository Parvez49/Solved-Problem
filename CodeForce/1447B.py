
for t in range(int(input())):
    n,m=map(int,input().split())
    l=list()
    neg=0
    s=0
    mi=1000

    for i in range(n):
        a = list(map(int,input().split()))
        for j in a:

            s += abs(j)
            if mi>abs(j):
                mi=abs(j);
            if j<0:
                neg+=1
    if neg%2==0:
        print(s)
    else:
        print(s-2*mi)



