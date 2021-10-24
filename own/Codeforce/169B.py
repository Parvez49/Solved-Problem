

n=list(input())
#s=input()
s=list(input())
#n=list(map(int,list(input())))
#s=list(map(int,list(input())))


s.sort(reverse=True)
#print(s)
sl=len(s)
k=0
for i in range(len(n)):
    if s[k]>n[i]:
        #n=n.replace(n[i],s[k],1)
        n[i]=s[k]
        k=k+1
    if k==sl:
        break

print(''.join(n))