


n=input()
print(len(n)*(int(n)+1)-int('1'*len(n)))







"""
for _ in range(int(input())):
    st=list(input())
    key=list(input())
    val=0
    for i in range(len(key)-1):
        #print(abs(st.index(key[i])-st.index(key[i+1])))
        val+=abs(st.index(key[i])-st.index(key[i+1]))
    print(val)
"""