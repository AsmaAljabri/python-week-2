# reading inputs from user and store it in a list for later process

value = []

print("please enter values, or Q to quit: ")
Userinput = input("enter value")

while Userinput.upper() != "Q" :
    value.append(float(Userinput))
    Userinput = input("enter value")
print("value = ",value)
