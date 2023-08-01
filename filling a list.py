# filling a list 
arr=[]
for i in range (0,11):
    
    n= i ** 2
       
    arr.append(n) 

print("arr = ", arr)

#ueing function to bulid up array 

def array( n ):
    arr = []
    for i in range ( n ):
        arr.append(i * i)
    return arr

result = array(11)
print(" the array = ",result)