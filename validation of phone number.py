# # Get user input for the phone number
# phone_number = input("Enter your phone number (format: (+000)0000-0000): ")




s = input("enter the number in format (+xxx)xxxx-xxxx : ")
valid = len(s) == 15
position = 0

while valid and position < len(s):
    if position == 0:
        valid = s[position] == "("
    elif position == 1:
        valid = s[position] == "+"    
    elif position == 5:
        valid = s[position] == ")" 
    elif position == 10:
        valid = s[position] == "-"
    else:
        valid = s[position].isdigit()
        position += 1 
    