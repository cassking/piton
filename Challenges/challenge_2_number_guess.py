"""
Number guessing game
The number to guess will be from 1 to 20 (inclusive).
The user will have 3 guesses to guess the number correctly.
After each wrong guess, the user will be told whether to
guess higher or lower next time.
If the user doesn't win, tell them the number.
"""
import random

correct = True
answer: int = random.randint(1, 3)


def loops():
    guess = int(input("Make a guess: "))
    if guess == answer:
        print(f"that is correct, game over the answer {answer}")
        return
    elif guess < answer:
        print(f"that number is lower than the number")
    elif guess > answer:
        print(f"that number is higher than the number")


def run_game():
    print("I'm thinking of a number between 1 and 20")

    for i in range(3):
        print(f"what is loop{i}")
        loops()
        if i == 2:
            print(f"the end {answer}")




run_game()
