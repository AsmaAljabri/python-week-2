# loop through the 2d list


matrix = [[1,2,3],
          [4,5,6]]
# to access the first row only 
for i in range (1) :
    for j in range (3):
        print(matrix[0][j], end=" ")
print("\n -"*2)
#acesss the first column only 
for i in range (2) :
    for j in range (1):
        print(matrix[i][0], end=" ")

#acesss the first column only 
print("\n -"*2)
for i in range (2) :
    for j in range (1):
        print(matrix[i][j], end=" ")
print("\n -"*2)

