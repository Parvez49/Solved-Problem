
for p in range(int(input())):
    #input()
    #input()
    a=list()
    for i in range(8):
        a.append(input())
    #print(p)
    #print(a)
    B=0
    for j in range(7,-1,-1):
        b=''
        if a[0][j]=="B":
            b=j
            c=0
            #print(b)
            for k in range(0,8):
                if a[k][b]=="B":
                    c+=1
            if c==8:
                print("B")
                B=1
                break
    if B==0:
        print("R")