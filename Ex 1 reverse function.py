# function to reverse a string
def reverse_str( string):
 
    return string[::-1]

user_input = input("enter the sentence you want to reverse")
ans = reverse_str(user_input)
print (ans)



x= 55 # returne the value x= 55 bc there is not parameters defined

def hi():
    return x

print(hi())

"""
def chair():
    pp =99
    return pp

chair()
print( pp )  # error bc pp is not definde outside of the function and it is not global
"""

# n = 4
# def f1():
#     n = n **4
#     print(n)   # output is error bc the n is not global and no parameter
# f1()

n = 4
def f1():
    global n 
    n = n **4
    print(n) 
f1()


x =12
def f11(a, b=x):
    print (a,b)

x= 15
f11(4)