# gussing game for random number 

import random


y = random.randint(0,10)

while 1 : # while true (1)
    
    x = input(" guess the randon number or done to end the game ")
    if int(x) > y :
        print(" the random number is less then the number")
    elif int(x)<y:
        print(" the random number is grater then the number")
    elif( int(x) == y ):
        print("correct, the numbers are equal",x , "=", y)    
        break

