import math

hh,mm=map(int,input().split())

h,d,c,n=map(int,input().split())
if hh<20:
    if mm!=0:
        mm=60-mm
        hh+=1
    mm = (mm + (20 - hh) * 60) * d
else: mm=0

#print(mm)
a=math.ceil(h/n)*c
#print(a)
b=(math.ceil((h+mm)/n)*c)
b-=b*0.2
if a<b: print("%.4f"%a)
else: print("%.4f"%b)