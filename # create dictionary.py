# create dictionary

contact = {"asma": 99887766
           ,"hilal":99774433
           ,"esra" : 99224455
           ,"ahmed" :99336644}

#duplicating dictionary

oldcontact = dict(contact)
print(oldcontact)
print("*" * 2 )
print(contact)

print("*" * 2 )

print("asma's phone is ",contact["asma"])
# to check the membershipe in contact if there are meny
print("*" * 2 )

if "ali" in contact :
    print("ali's phone is", contact["ali"])
else:
    print("contact is not founded")

if "asma" in contact :
    print("Asma's phone is ", contact["asma"])
else:
    print("contact is not founded")

print("*" * 2 )

# defualt key when search for a number 
number = contact.get("ali", "number is not found")
print("dial" + str(number))

number = contact.get("asma", "number is not found")
print("dial   " + str(number))

print("*" * 2 )

# add or modifying items 

#add
contact["ali"]= 12345678

#modify
contact["asma"] = 99887755

print(contact)

print("*" * 2 )

# removing element

contact.pop("esra")

print(contact)

print("*" * 2 )

# remove but store element as variable to use it later but you remove it from contract

Alinumber = contact.pop("ali")
print(contact)
print("*" * 2 )

# traversing a dict and sort then using loop

print("my contacts: ")
for key in sorted(contact):
    print(key, contact[key])

print("*" * 2 )

# iterating the dict using item() method 

for item in contact.items():
    print(item[0],item[1])
