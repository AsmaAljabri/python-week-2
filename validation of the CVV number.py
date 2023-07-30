s = input("enter the CVV number in the format xxxx-xxx : ")
valid = len(s) == 8
position = 0


while valid and position < len(s):
    if position == 4:
        valid = s[position] == "-"

    else:
        valid = s[position].isdigit()
    position += 1 
if valid:
    print(" the CVV of the card is a valid number")
else:
    print(" the CVV of the card is not valid number")
