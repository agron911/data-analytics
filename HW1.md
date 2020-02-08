# data analytics
####  Q4 Write a Python program to find a word which has the most number of letters from a list of words
```py
#def search(sequence):
#    return(len(sequence))


list1= ['today','is','a','good','day']
ans=sorted(list1,reverse=True)

#ans=sorted(list1,key = search,reverse=True)

print(ans[0])

```

#### Q5   Write a Python program to print all common values in a dictionary 
```py
dic = {'0':'today', '1':'is','2':'a','3':'good','4':'good','5':'good','6':'day','7':'day'}
dic1 = {'11':'today', '1':'is','2':'a','3':'good','4':'good','5':'good','6':'day','7':'day'}


l=list(dic.values())
d = {}
for key in l:
    d[key] = d.get(key, 0) + 1

for k, v in d.items():
    if v > 1:
        print(k)

```

#### Q6    Write a Python program to combine two dictionaries based on their keys, if two keys are the same, sum their values together 
```py
from collections import Counter

dict1 = {'today': 12, 'is': 25, 'good': 9} 
dict2 = {'a': 100, 'good': 200, 'day': 300} 
d = Counter(dict1) + Counter(dict2)
          
d 

```

#### Q7 Write a Python program to remove tuple(s) which has certain given value from a list of tuples 
```py
t = ("today","is","a","good","good","day")
t = t[:3] + t[3:]
tuplis = list(t)
rem=input("enter the word you want to remove:")
tuplis.remove(rem)

tuplis
```