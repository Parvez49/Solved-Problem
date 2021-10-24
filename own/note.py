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

