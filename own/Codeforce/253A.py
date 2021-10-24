

i=open("input.txt",'r')
o=open("output.txt",'w')
n,m=map(int,i.readline().split())

if n==m:
    st=["GB"]*n
    o.write(''.join(st))
else:
    if n>m:
        st=["BG"]*m
        st+=["B"]*(n-m)
        o.write(''.join(st))
    else:
        st=["GB"]*n
        st+=["G"]*(m-n)
        o.write(''.join(st))