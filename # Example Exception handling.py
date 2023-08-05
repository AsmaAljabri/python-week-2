# Example Exception handling 

inputOk = False
while (inputOk == False):
    try:
        num = input("enter a number")
        num = float(num)
        inputOk = True #all characters are part of numbers
    except ValueError: # can't convert toa number
        print("non-numeric type enterd '%s'" %num)

num =num * 2
print(num)
