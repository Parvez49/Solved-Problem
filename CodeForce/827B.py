for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    s=set()
    for i in a:
        s.add(i)
    if len(s)==n:
        print("YES")
    else:print("NO")