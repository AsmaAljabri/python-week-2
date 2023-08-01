# linear search
limit = 90
pos = 0
found = False

list = [10, 20, 30, 40, 50, 90, 80, 100]

while pos <len(list) and not found : #not found is the key to find the limit in list and stop the loop
    if list[pos] == limit :
        found = True
    else:
        pos += 1
if found :
    print("found at position ", pos)
else:
    print("not found")

    