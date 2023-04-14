#secret number ==
secret_number = 10
user_input = input("try to find the secret number between 1 and 10: ")

if secret_number == int(user_input):
    print("Great ! you win !")
else:
    print("You loose !")

print("Try to play again !")



#secret number !=
secret_number = 10
guess = input("try to find the secret number between 1 and 10 :")

if secret_number != int(guess):
    print("you don't find it ! try again !")
else:
    print("Congratulations ! You win !")

print("Would you play again ?")