# function for vowls



from collections import Counter



def count_vowls(sentence):
    sentence = sentence.lower()
    arr=[]
    count_arr = 0
    vowls ="a","i","o","u","e"
    for i in sentence:
        if(i in vowls):
            print(i) 
        
            arr.append(i)  

    count_arr = Counter(arr)
    return count_arr

sentence =input("eenter the sentence") #" hello python"
s = count_vowls(sentence)
print(s)
