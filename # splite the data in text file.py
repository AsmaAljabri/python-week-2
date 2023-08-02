# splite the data in text file
file_splite = open("exs in file to splite.txt","r")

for line in file_splite:
    data = line.rsplit()
    print(data[0])
    print(line[0])
file_splite.close()


