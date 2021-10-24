
def dsum(a):
    d=0
    while(a):
        d+=a%10
        a=int(a/10)
    return d
n=int(input())

x=0
while(x*10+9<=n):
    x=x*10+9
#print(sum(map(int,list(str(x)))) + sum(map(int,list(str(n-x)))))
print(dsum(x)+dsum(n-x))