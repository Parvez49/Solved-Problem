


n=int(input())
c=0
for i in range(n):
    r,p=map(int,input().split())
    if r+p+1>n:
        c+=1
print(c)







"""
n=int(input())
arr=list(map(int,input().split()))
carr=[0]*n
for i in arr:
    carr[i-1]+=1

def ispalin(arr):
    s=len(arr)
    for i in range(s//2):
        if arr[i]!=arr[s-1]:
            return False
        s-=1
    return True

if ispalin(arr):
    print("yes")
else:
    for i in range(10):
        if carr[i]<2:
            continue
        else:
            for j in range(1,carr[i]+1,2):
                

"""


