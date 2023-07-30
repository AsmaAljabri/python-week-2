import math

def area_of_regular_polygon(num, side):
                                                # Calculate the area using the formula
    area = (num * side**2) / (4 * math.tan(math.pi / num))
    return area, num, side_length

num = int(input("Enter the number of sides of the regular polygon: "))
side_length = float(input("Enter the length of one side of the regular polygon: "))

polygon_area = area_of_regular_polygon(num, side_length)
print("The area of the regular polygon is:", polygon_area)
