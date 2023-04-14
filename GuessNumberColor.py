number = 24
color = "green"

guess1 = input("Try to find the right number: ")
guess2 = input("Try to find the right color: ")

if number == int(guess1) and color == guess2:
    print("You've found both secret number and secret color !")
elif number == int(guess1) or color == guess2:
    print("You've found at least one of the secrets ! ")
else:
    print("You didn't find any of the secrets")
    print("Better luck next time !")

print ("Try again !")

#to wrap this in a fonction
#give a function with its name and correct all the indents, and don't
#forget to ask the function at the end ;)
#you'll find it in the file GuessNumberColorFunction.py