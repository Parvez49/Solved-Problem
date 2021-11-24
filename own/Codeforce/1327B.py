
for _ in range(int(input())):
    n=int(input())
    pr=[0]*(n)

    co=0
    rg=0
    for i in range(n):
        a=list(map(int,input().split()))
        a[1:]=sorted(a[1:])
        ck=0
        for j in range(1,len(a)):
            if not pr[a[j]-1]:
                pr[a[j]-1]=1
                #couple[i+1]=a[j]
                co+=1
                ck=1
                break
            #print(pr)
        if ck==0 and not rg:rg=i+1

    if co==n:
        print("OPTIMAL")
    else:
        print("IMPROVE")
        for i in range(len(pr)):
            if not pr[i]:
                print(rg,i+1)
                break