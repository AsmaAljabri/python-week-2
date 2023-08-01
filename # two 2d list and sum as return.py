# # two 2d list and sum as return 

m = [[1,2,3],
     [4,5,6]]

x = [[1,2,3],
    [4,5,6]]
def sum_2d(list1, list2):
    
    if len(list1) == len(list2) and len(list1[0]) == len(list2[0]) and len(list1[1]) == len(list2[1]):
        
        arr= [[0,0,0],[0,0,0]]
        for n in range (len(list1)) :
            for b in range (len(list2[0])):
                arr[n][b] = list1[n][b] + list2[n][b]
        return arr         
    else:
        
        print("Error")
        
     

lists = sum_2d(m,x)
print(lists)






        