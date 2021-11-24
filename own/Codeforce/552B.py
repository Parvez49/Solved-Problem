
n=input()
nl=len(n)
n=int(n)
if nl==1:
    print(n)
elif nl==2:
    print(2*n-9)
else:
    s=189
    ten=100
    nine=900
    nl=nl-3
    a=0
    for i in range(nl):
        s+=(nine*(i+3))
        nine*=10
        ten*=10
        a=i+1
    n=n-ten+1
    a=a+3
    s+=n*a
    print(s)



