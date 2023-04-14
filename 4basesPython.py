#base
message = "coucou"
print(message)
message = 12
print(message)

#base fonction
def say_coucou(name):
    print("Hey "+name)
say_coucou("Georges")
say_coucou("Betty")

#base fonction avec plusieurs paramètres et la notion de "result"
def say_hello(name, secondname):
        result = "Hello "+name+secondname
        print(result)
say_hello("Georges "+"Ofthejungle")


#base fonction avec la fonction return
def helllo(firstname, nickname):
    result = firstname+nickname
    return result
print(helllo("Georges "+"Ofthejungle"))
print(helllo)("Betty "+"Ofthemountain")