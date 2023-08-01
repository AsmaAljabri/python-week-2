# program to git the type of data in list

list = [1.4,4,5,"name","asma"]

i = 0
for i in list:
    if type(i) == str:
        print(i)
    
list = [1.4, 4, 5, "name", "asma"]

for i in range(len(list)):
    if type(list[i]) == str:
        print(list[i])
