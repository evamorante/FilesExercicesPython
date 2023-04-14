#number = input("Type a number: ")
#result = int(number) + 1
#print("The result is " + str(result))

#if the user put a word-so a string-so an unvalid entry-
#  we will use the try/except block

number = input("Type a number: ")

try:
    result =int(number) + 1
except:
    print("Couldn't convert your input to a valid number")
    quit()

print("The result is " + str(result))