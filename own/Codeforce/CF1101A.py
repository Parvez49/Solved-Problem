import math
for i in range(int(input())):
    l,r,d=map(int,input().split())

    if l>d:
        print(d)
    else:
        if l<=d:
            if r%d==0:
                print((int(r/d)+1)*d)
            else:
                print(math.ceil(r/d)*d)




