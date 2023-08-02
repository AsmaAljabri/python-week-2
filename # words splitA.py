# words splitA

input_f = open("words splitA.txt","r")

for line in input_f:
    data = line.rsplit()

print(data)


