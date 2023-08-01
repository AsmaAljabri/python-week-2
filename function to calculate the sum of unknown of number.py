#  function to calculate the sum of unkown integers

def calculate_sum(*args):
    total = 0
    for num in args:
        total += num
    return total


result = calculate_sum(1, 2, 3, 4, 5)
print("The sum is =", result)
