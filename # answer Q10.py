# answer Q10
def find_longW(Wordlist, n):
    Words = []
    for word in Wordlist:
        if len(word) > n:
            Words.append(word)
    return Words

Wordlist = input("Enter a list of words separated by spaces: ").split()

# Get the value of n from the user
n = int(input("Enter the value of n: "))

result = find_longW(Wordlist, n)

# Print the result
print("Words longer than",n," words = ",result)


