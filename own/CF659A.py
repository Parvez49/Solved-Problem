n,a,b=map(int,input().split())
if b<0:
    if abs(b)-a==0:
        print(n)
    else:
        print(n-(abs(b)-a)%n)
else:
    if (a+b)%n==0:
        print(n)
    else:
        print((a+b)%n)