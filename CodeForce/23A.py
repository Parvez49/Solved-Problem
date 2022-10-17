for _ in range(int(input())):
    input()
    a=input()
    a=a.replace(" ","")
    a=list(a)
    z,o=0,0
    op=0
    for i in a:
        if i=='0':
            z+=1

    while True:
        if ('0' not in a) or z==0:
            print(op)
            break
        elif a.index('0')!=0:
            op+=1
            z-=1
            a=a[1::]
            a=a[::-1]
            if a.index('0')!=-1:
                a[a.index('0')]="1"
                a=a[::-1]
        else:a=a[1:]