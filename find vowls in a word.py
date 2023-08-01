# program to find vowls in a word
from collections import Counter


s = " hello python"


s = s.lower()
arr=[]
count_arr = 0
vowls ="a","i","o","u","e"
print(vowls)
for i in s:
    if(i in vowls):
        print(i) 
       
        arr.append(i)   
# for i in arr:

count_arr = Counter(arr)

print(count_arr)

print(arr)

    
