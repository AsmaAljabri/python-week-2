# answer Q 6
def count_zeros(list):
    count = 0
    for i in list:
        if i == 0:
            count += 1

    return count

my_list = [0, 2, 0, 5, 0, 7, 0, 0]
zero_count = count_zeros(my_list)
print("Number of elements equal to zero:", zero_count)
