"""
Guess the number between 1 and 10
"""

import random
answer = random.randint(1, 10)

guess = int(input("I'm thinking of a number between 1 and 10: "))

# If the number is correct, tell the user
# Otherwise, tell them if the answer is higher or lower than their guess
if guess == answer:
    print(f"the guess was same as {answer} that is correct")
elif guess < answer:
    print(f"the guess was lower than the answer which was {answer}")
elif guess > answer:
    print(f"the guess was higher than the answer which was {answer}")



print('The number was {}'.format(answer))
