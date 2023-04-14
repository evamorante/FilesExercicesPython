#setup -- OK
import random
answer = random.randint(1,100)
user_wins = False
attempts = 0
attempt_word = ""



#game loop -- OK
while user_wins != True :

    #get user input -- OK
    guess = input("Enter a number between 1 and 100 : ")

    #check the user input  -- OUBLIÉ
    try:
        guess_number = int(guess)
    except:
        print("Error: You need to enter a valid number!")
        quit()

    #increase attempt count  -- NO IDEA
    attempts += 1

    #check the user answer against the secret number -- OK
    if guess_number == answer:
        user_wins = True
    elif guess_number > answer:
        print("The secret number is smaller!")
    else:
        print("The secret number is bigger!")

#get the spelling of the "attempt" word -- A CREUSER EN REVENANT 
# SUR LES MODULES/MOD 8 LOOP LESSONS
if attempts == 1:
    attempt_word = " attempt"
else: 
    attempt_word = " attempts"

#display the result -- OK
print("You won !! You took " + str(attempts) + attempt_word)
