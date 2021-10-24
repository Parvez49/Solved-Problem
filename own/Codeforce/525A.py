
n=int(input())

str=input()
str2=str
k=0
l= [0]*26
#print(l)
for i in range(0,len(str)):
    if i%2==1:
        if l[ord(str[i])-ord('A')]==0:
            k+=1
        else: l[ord(str[i])-ord('A')]-=1
    else:
        l[ord(str[i])-ord('a')]+=1
print(k)