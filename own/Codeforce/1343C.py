for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))

    if n==1:
        print(a[0])
        continue
    if n==2:
        if a[0]>0 and a[1]>0:print(max(a))
        elif a[0]<0 and a[1]<0: print(max(a))
        else:print(sum(a))
        continue
    else:
        s=0
        pval=a[0]
        if pval>0:psign=0
        else:psign=1
        for i in range(1,n):
            if a[i]>0:csign=0
            else:csign=1
            if psign==csign:
                pval=max(pval,a[i])
                if i==n-1:s+=pval
            else:
                #print(pval)
                s+=pval
                psign=csign
                pval=a[i]
        if a[n-1]>0 and a[n-2]<0 or a[n-1]<0 and a[n-2]>0:
            s+=a[n-1]
    print(s)