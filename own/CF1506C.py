
for i in range(int(input())):
    str1=input()
    str2=input()
    if str1==str2:
        print(0)
    else:

        mat=[[0 for i in range(len(str1)+1)] for i in range(len(str2)+1)]

        max=0
        for i in range(len(str2)):
            for j in range(len(str1)):
                if str2[i] == str1[j]:
                    mat[i+1][j+1]=mat[i][j]+1
                    if max<mat[i+1][j+1]:
                        max=mat[i+1][j+1]
        print(len(str1+str2)-2*max)



