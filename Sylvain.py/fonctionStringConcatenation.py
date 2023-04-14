def hello(name1, name2):
    result = (name1+name2)
    print("Hello"+result)
hello(" Jackie", " James") 

# variable globale my_name dans le corps de la fonction
# avant le print()
def say_hello():
    my_name = " Jim"
    print("Hello"+my_name)
say_hello()