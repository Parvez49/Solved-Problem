import math

for i in range(int(input())):
    n=int(input())
    print(math.ceil(2*(math.sqrt(n)-1)))


3 3
1 2 3
2 3 4
3 4 2

4 5
1 3 5 6 7
3 0 7 0 9
5 0 0 0 10
8 9 10 11 12

for p in range(int(input())):
    n,m,k=map(int,input().split())
    if n==1 and k==2 and m==0:
        print('YES')
    elif m<n-1 or k<3 or m>n*(n-1)/2:
        print('NO')
    elif  k==3 and m<n*(n-1)/2:
        print('NO')
    else:
        print('YES')

"""
n=1111
d=6
c=10
k=1

for i in range(150):
    n+=1
    c+=1
    print(n)

    if(n%(10*k)==6*d):
        d=d*10+1
        k*=10
        n+=34


5 1
polandball
is 
a
cool 
character
hope

2 2
kremowka
wadowicka
kremowka
wiedenska

1 2
a
a
b
"""

n=int(input())

set1=set()
set2=set()
sel=0
for i in range(n-1):
    u,v=map(int,input().split())
    if u not in set1 and u not in set2 and v not in set1 and v not in set2:
        set1.add(u)
        set2.add(v)
    elif (u in set1 and v in set1) or (u in set2 and v in set2):
        sel+=1
    else:
        if u in set1:
            set2.add(v)
        elif u in set2:
            set1.add(v)
        if v in set1:
            set2.add(u)
        elif v in set2:
            set1.add(u)


    #print(set1)
    #print(set2)
#l1=len(set1)
#l2=len(set2)
print((n*n)//4-(n-1)-sel)
#print(l1*l2-(n-1))

