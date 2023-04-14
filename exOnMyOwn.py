coucou = ("message")
print(coucou)
coucou = 12
print(coucou)

def say_coucou(name):
    print("Hey "+name)
say_coucou("Georges")
say_coucou("Betty")

def say_coucou(name, familyname):
    result = name+familyname
    print(result)
say_coucou("Georges ","Ofthejungle")
say_coucou("Betty","Ofthemountain")
def say_hello(name, familyname):
    result = "Hello "+name+familyname
    return result
print(say_hello("Georges ","ofthejungle"))