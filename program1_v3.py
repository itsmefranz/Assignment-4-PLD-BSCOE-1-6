def getNameAgeAddress():
    _name= input("Name: ")
    _age= int(input("Age: "))
    _add= input("Address: ")
    return _name, _age, _add

def display(name_, age_, add_):
    print(f"Hi, my name is {name_}. I am {age_} years old and I live in {add_}.")

name, age, address= getNameAgeAddress()
display(name, age, address)