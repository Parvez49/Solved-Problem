

n=int(input())
li=list(map(int,input().split()))
cli=[1]*n
for i in range(n-1):
        if li[i+1]<=li[i]*2:
            cli[i+1]+=cli[i]
print(max(cli))
