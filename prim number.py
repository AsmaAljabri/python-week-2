"""
Write Python code that go throw all numbers from 1 to 30
and print True if the number is prime and False if not. 
The output format should be like the following:
"""
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

for num in range(1, 31):
    print(num,"  |  ", is_prime(num))



