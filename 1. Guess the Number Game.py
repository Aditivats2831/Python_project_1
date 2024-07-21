'''  1. Guess the Number Game
Description: A game where the computer randomly selects a number and the user has to guess it with hints provided.  '''

import random
computer_num = random.randrange(0,101)

print("hey! I am computer , I have a no. in my mind can you guess it")


while True :
    user_num = int(input("Enter any no. guess by you : "))

    if(user_num == computer_num):
        print("yee! you guess the right no.")
        break
    elif(user_num < computer_num):
        print("your no. is smaller then my no.")

    else :
        print("your no. is larger then my no. ")

print("Hope you enjoy the game")
