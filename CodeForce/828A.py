
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    s=input()
    ad=dict()
    sd=dict()
    for i in range(len(a)):
        try:
            ad[a[i]].append(i)
        except :
            ad[a[i]]=[i]
    #print(ad)
    if len(ad.keys())==n:
        print("YES")
    else:
        ind=0
        pr=0
        for i in range(len(s)):
            try:
                if sd[i]!=s[i]:
                    #print("NO")
                    pr=1
                    break
            except:
                for j in ad[a[i]]:
                    sd[j]=s[i]
            ind+=1
        if ind==n and pr==0:
            print("YES")
        else:print("NO")
        #print(ind)
