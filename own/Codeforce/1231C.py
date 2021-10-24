


n,m=map(int,input().split())
mat=list()

for i in range(n):
    a=list(map(int,input().split()))
    mat.append(a)

k=1
for i in range(n-2,-1,-1):
    for j in range(m-2,-1,-1):
        d,r=0,0
        if mat[i][j]==0:
            #print(i,j)
            x=min(mat[i+1][j],mat[i][j+1])
            x-=1
            #print(x)
            if (mat[i-1][j]!=0 and mat[i-1][j]<x) or mat[i-1][j]==0:
                #print("jdfs")
                d=1
            else: d=0

            if (mat[i][j-1]!=0 and mat[i][j-1]<x) or mat[i][j-1]==0:
                #print("dksf")
                r=1
            else: r=0
            #print("dr")
            #print(d,r)
            if d==0 or r==0:
                print(-1)
                exit()
            else:
                mat[i][j]=x
        else:
            #print(i,j)
            if mat[i][j]>=mat[i+1][j] or mat[i][j]>=mat[i][j+1]:
                #print("last if")
                print(-1)
                exit()
if mat[n-1][m-1]<=mat[n-2][m-1] or mat[n-1][m-1]<=mat[n-1][m-2]:
    print(-1)
else: print(sum(map(sum,mat)))
#print(mat)