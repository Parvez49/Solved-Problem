
def rec(a,sta,rema,v,j):
    if len(rema)==2:
        if abs(v - rema[j]) == 1 or v % 2 == rema[j] % 2:
            print("Yes")
            return
        else:
            return
    if j==len(rema):
        return
    else:
        if abs(v - rema[j]) == 1 or v % 2 == rema[j] % 2:
            sta.append(v)
            sta.append(rema[j])
            rema.remove(v)
            rema.remove(rema[j - 1])
            print(sta)
            print(rema)
            rec(a,sta, rema, rema[0], 1)
        else:
            rec(a,sta, rema, rema[0], j + 1)
    sta=[]
    rec(a,sta,a,a[0],j+1)







def s(a,n):
    j=1
    rema = a
    sta =list()
    v=a[0]
    rec(a,sta,rema,v,j)



n=int(input())
a=list(map(int,input().split()))
s(a,n)







"""

    if abs(v - a[j]) == 1 or v % 2 == a[j] % 2:
        sta.append(v)
        sta.append(a[j])
        rema.remove(v)
        rema.remove(a[j])
        rec(sta,rema, rema[0], 1)
        print("g")
        
        
        
n=int(input())
a=list(map(int,input().split()))

while(1):
    i=a[0]
    le=len(a)
    for j in range(1,len(a)):
        if abs(i-a[j])==1 or i%2==a[j]%2:
            a.remove(a[j])
            a.remove(i)
            break
    if le==len(a):
        print("NO")
        exit()
    if len(a)==0:
        print("yes")
        break
"""