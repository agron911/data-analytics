#!/usr/bin/env python3

s = 'MCMXCIV'
res = 0
lis = []
num = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
for i in s:
    lis.append(num[i])
for i in range(0,len(lis)-1):
    if lis[i] < lis[i+1]:
        res -= lis[i]
        continue    
    res +=lis[i]
    
res+= lis[len(lis)-1]
print(res)