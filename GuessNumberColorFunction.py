def play():
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

    play()

    #doesn't work ?!!!