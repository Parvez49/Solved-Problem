
class Solution:
    def romanToInt(self, s: str) -> int:
        d=dict()
        d["I"]=1
        d["V"]=5
        d["X"]=10
        d["L"]=50
        d["C"]=100
        d["D"]=500
        d['M']=1000

        num=0
        i=len(s)-1
        while(i>=1):
            if d[s[i]]<=d[s[i-1]] :
                num+=d[s[i]]
            else:
                num+=d[s[i]]- d[s[i-1]]
                i-=1
            i-=1
        if i==0:
            num+=d[s[i]]
        return num
