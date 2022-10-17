for _ in range(int(input())):
    n=int(input())
    res=list()
    res.append(1)
    for i in range(1,n+1,2):
        if i+2<=n:
            res.append(i+2)
    #print(res,i)
    if i==n:
        i-=1
    else:i+=1
    for j in range(i,0,-2):
        if j>0:
            res.append(j)
    for i in range(len(res)-1):
        print(res[i],end=" ")
    print(res[i+1])