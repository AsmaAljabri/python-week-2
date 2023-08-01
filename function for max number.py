# functin to get the max number between 3 inputs

A = int(input("enter the value for A"))
B = int(input("enter the value for B"))
C = int(input("enter the value for c"))




def get_maximum_number(A, B, C = 2): # c = 2 is a defualt number for C in the user only enter 2 numbers
    if A >= B and A >= C:
        return A
    elif B >= A and B >= C:
        return B
    else:
        return C

    # return max(A, B, C)



maximum_number = get_maximum_number(A, B, C)
print("The maximum number is:", maximum_number)
