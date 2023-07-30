# implement and test function

def volum_cub(sidelength):
    volume = sidelength **3
    return volume

result = volum_cub(3)
print("the volume = ", result)


name = "asma"

def say_hi(nam):
    return "Hi " + name

person = say_hi(name)
print(person )