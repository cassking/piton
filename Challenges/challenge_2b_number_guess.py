"""
Number guessing game
The number to guess will be from 1 to 20 (inclusive).
The user will have 3 guesses to guess the number correctly.
After each wrong guess, the user will be told whether to
guess higher or lower next time.
If the user doesn't win, tell them the number.
"""
# second version based on video
import random


def run_game():
    answer: int = random.randint(1, 20)
    print("I'm thinking of a number between 1 and 20")
    number_guesses = 3
    while number_guesses > 0:
        print(f'you have {number_guesses} left')
        guess = int(input("Make a guess: "))
        if guess == answer:
            print(f"that is correct, game over the answer {answer}")
            return
        elif guess < answer:
            print(f"that number is lower than the number")
        else:
            print(f"that number is higher than the number")
        number_guesses -= 1
        if number_guesses < 1:
            print("game ended")

run_game()
