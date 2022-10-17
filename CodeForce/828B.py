
for _ in range(int(input())):
    n,nq=map(int,input().split())
    a=list(map(int,input().split()))
    q=list()
    for i in range(nq):
        q.append(list(map(int,input().split())))
    #q=list(map(int,input().split()))
    #print(q)
    odd,even=0,0
    sev,sod=0,0
    for i in a:
        if i%2==0:
            even+=1
            sev+=i
        else:
            odd+=1
            sod+=i
    #print(sev,sod)


    for i in q:
        if i[0]%2==0:
            sev += i[1] * even
            if i[1]%2==1:
                odd+=even
                even=0
        else:
            sod+=i[1]*odd
            if i[1]%2==1:
                even+=odd
                odd=0
        print(sev+sod)