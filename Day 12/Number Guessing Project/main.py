import random
from art import logo, logo2

def difficulty():
    dif = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if dif == "easy":
        tries = 10
    else:
        tries = 5
    return tries

def com_guess():

    guessed_num = random.randint(0,100)
    return guessed_num

def guess_compare(cpu_num,my_lives):
    while my_lives > 0:
        my_guess = int(input(f"You have {my_lives} attempts remaining to guess the number.\n"
                             f"Make a guess: "))
        if my_guess == cpu_num:
            print(f"You got it! The answer was {cpu_num}")
            break
        elif my_guess < cpu_num:
            print("Too low.")
            my_lives -= 1
        else:
            print("Too high.")
            my_lives -= 1
        if my_lives == 0:
            print(f"You have run out of guesses. The correct number was {cpu_num}")
        else:
            print("Guess again")









is_game_over = False
while not is_game_over:
    print(logo)
    print("Welcome to the Number Guessing Game!!\n"
          "I'm thinking of a a number between 1 and 100.")
    com_num =com_guess()
    lives = difficulty()
    guess_compare(com_num, lives)
    while input("Do you want to play another round? Answer with 'y' or 'n': ") == "n":
        is_game_over = True
        print("See you next time...")
        print(logo2)
        break
