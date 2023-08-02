# average_num:


ave_file = open("average_num.txt","r")
# line = ave_file.readline() this will skip the first line 
sum = 0 
l= 0 

for line in ave_file:

    sum += float(line)
    l += 1

result = sum / l
print(result) #69.75
print(sum)# 348.75

ave_file.close()

