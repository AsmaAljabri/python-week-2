# ex on dict
dec = { 1 :{"name": "john","age":27,"sex":"male"},
        2 :{"name": "maria","age":22,"sex":"female"},
        3 :{"name": "sali","age":23,"sex":"female"}}


print("my contacts: ")

for item in dec:
    if dec[item]["age"] > 22:
        print( dec[item]["name"])

print("*" * 2 )

# # Convert dictionary items to a list of tuples
# sorted_items = list(dec.items())

# # Perform a simple selection sort based on age
# for i in range(len(sorted_items)):
#     min_idx = i
#     for j in range(i+1, len(sorted_items)):
#         if sorted_items[j][1]["age"] < sorted_items[min_idx][1]["age"]:
#             min_idx = j
#     sorted_items[i], sorted_items[min_idx] = sorted_items[min_idx], sorted_items[i]

# # Create a new dictionary from the sorted list of tuples
# sorted_dec = dict(sorted_items)

# print(sorted_dec)

sorted_dec = dict(sorted(dec.items(), key=lambda item: item[1]["age"]))
print(sorted_dec)

   