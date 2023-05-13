def add(n1,n2):
    result = n1+n2
    return result
total = add(5,8)
print(total)


def greet(name, weather):
    message = "Hi "+name+".It is a "+weather+" day."
    return message
greetings = greet("Sasha","rainy")
print(greetings)
greetings = greet("Carl","sunny")
print(greetings)
print(greet("Sasha","rainy"))
print(greet("Thomas","cloudy"))
print(greetings+" Better well dress in")


#exercise with using a return function rather than displaying the result 
#from within the functions 
#one line empty separating the first exercise to the "return"exercise
def substract(number_one, number_two):
    result = number_one-number_two
    print(result)
substract(5,3)
substract(11.2,8.8)
substract(10, -10)

def substract(number_one, number_two):
    result = number_one-number_two
    return result
substraction = substract(45,23)
print(substraction)

def multiply(number_one, number_two, number_three):
    result = number_one*number_two*number_three
    print(result)
multiply(5,3,2)
multiply(11.2,8.8,4)
multiply(10, -10,6)

def multiply(number_one, number_two, number_three):
    result = number_one*number_two*number_three
    return result
multi = multiply(4,6,13)
print(multi)

def add(n1,n2):
    result = n1+n2
    return n1+n2
total = add(5,8)
print(total)

def add(n1,n2):
    result = n1+n2
    return n1+n2
print(add(5,8))
print(add(7,9))
print(add(11,20))