words = ['account', 'addition', 'adjustment', 'advertisement', 'agreement',
         'amount', 'amusement', 'animal', 'answer', 'apparatus', 'approval',
         'argument', 'attack', 'attempt', 'attention', 'attraction',
         'authority', 'balance', 'behavior', 'belief', 'breath', 'brother',
         'building', 'business', 'butter', 'canvas', 'chance', 'change',
         'comfort', 'committee', 'company', 'comparison', 'competition',
         'condition', 'connection', 'control', 'copper', 'cotton', 'country',
         'credit', 'current', 'damage', 'danger', 'daughter', 'decision',
         'degree', 'design', 'desire', 'destruction', 'detail', 'development',
         'digestion', 'direction', 'discovery', 'discussion', 'disease',
         'disgust', 'distance', 'distribution', 'division', 'driving',
         'education', 'effect', 'example', 'exchange', 'existence', 'expansion',
         'experience', 'expert', 'family', 'father', 'feeling', 'fiction',
         'flight', 'flower', 'friend', 'government', 'growth', 'harbor',
         'harmony', 'hearing', 'history', 'impulse', 'increase', 'industry',
         'insect', 'instrument', 'insurance', 'interest', 'invention',
         'journey', 'knowledge', 'language', 'learning', 'leather', 'letter',
         'liquid', 'machine', 'manager', 'market', 'measure', 'meeting',
         'memory', 'middle', 'minute', 'morning', 'mother', 'motion',
         'mountain', 'nation', 'number', 'observation', 'operation', 'opinion',
         'organisation', 'ornament', 'payment', 'person', 'pleasure', 'poison',
         'polish', 'porter', 'position', 'powder', 'process', 'produce',
         'profit', 'property', 'protest', 'punishment', 'purpose', 'quality',
         'question', 'reaction', 'reading', 'reason', 'record', 'regret',
         'relation', 'religion', 'representative', 'request', 'respect',
         'reward', 'rhythm', 'science', 'secretary', 'selection', 'servant',
         'silver', 'sister', 'sneeze', 'society', 'statement', 'stitch',
         'stretch', 'structure', 'substance', 'suggestion', 'summer', 'support',
         'surprise', 'system', 'teaching', 'tendency', 'theory', 'thought',
         'thunder', 'transport', 'trouble', 'vessel', 'weather', 'weight',
         'winter', 'writing']

hard_words = ['Awkward', 'Bagpipes', 'Banjo', 'Bungler', 'Croquet', 'Crypt',
              'Dwarves', 'Fervid', 'Fishhook', 'Fjord', 'Gazebo', 'Gypsy',
              'Haiku', 'Haphazard', 'Hyphen', 'Ivory', 'Jazzy', 'Jiffy', 'Jinx',
              'Jukebox', 'Kayak', 'Kiosk', 'Klutz', 'Memento', 'Mystify',
              'Numbskull', 'Ostracize', 'Oxygen', 'Pajama', 'Phlegm', 'Pixel',
              'Polka', 'Quad', 'Quip', 'Rhythmic', 'Rogue', 'Sphinx', 'Squawk',
              'Swivel', 'Toady', 'Twelfth', 'Unzip', 'Waxy', 'Wildebeest',
              'Yacht', 'Zealous', 'Zigzag', 'Zippy', 'Zombie']

"""
Word guessing game
------------------
Choose a word for the user to guess.
The user can have 6 wrong guesses before they lose the game.
After each guess, display the correct guesses, the wrong guesses,
and the number of wrong guesses left.
If the user doesn't win, tell them the answer.
"""
import random


def user_did_win(answer, guessed_letters):
    for letter in answer:
        if letter not in guessed_letters:
            return False
    return True


# tests can write this way because user_did_win returns a boolean
assert(user_did_win('hi', ['h', 'i', 's']) == True)
assert(not user_did_win('hi', ['i', 's']) == False)


def word_game():
    answer = random.choice(words)
    num_wrong_guesses_left = 6
    guessed_letters = []
    print(f'answer: {answer}')

    while num_wrong_guesses_left > 0:
        display_word = ""
        for letter in answer:
            if letter in guessed_letters:
                print(f"guessed letters {guessed_letters}")
                display_word += letter
            else:
                display_word += '_'

        print(display_word.strip())
        print(f'{num_wrong_guesses_left} wrong guesses left')
        print(f'Guesses: {guessed_letters}')

        guess = input("Guess a letter: ")
        guessed_letters.append(guess)

        if guess in answer:
            print("Correct!")
        else:
            print("Nope :(")
            num_wrong_guesses_left -= 1

        if user_did_win(answer, guessed_letters):
                print("You win!")
                return
    print("Sorry, you lose")
    print(f"The answer was {answer}")


word_game()