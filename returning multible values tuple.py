# returning multible values

def readdate():
    print("enter a date:")
    month= int(input("month: "))
    day= int(input("day: "))
    year=int(input("year: "))
    return (month,day,year) #return tuple

#function call by assign entire value to a tuple
date = readdate()

print(date)
#call funcrion 
(month, day, year) = readdate()

print(month)