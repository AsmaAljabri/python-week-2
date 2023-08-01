# calculate average

num =5
list = [50,88,98,78,67]

def cal_aver(value, n):
    sum = 0
    for i in range (0,n):
        sum += value[i] 
    average = sum / n 
    return average

class_aver = cal_aver(list, num)

print("the average = ", class_aver)