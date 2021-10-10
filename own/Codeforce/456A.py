
n=int(input())


for i in range(n):
    a=list(map(int,input().split()))
    if a[0]!=a[1]:
        print("Happy Alex")
        exit()
print("Poor Alex")