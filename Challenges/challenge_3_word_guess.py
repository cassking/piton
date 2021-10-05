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
Word guessing game (hangman)
Choose a word for the user to guess.
The user can have 6 wrong guesses before they lose the game.
User guesses one letter at a time
After each guess, display the correct guesses, the wrong guesses,
and the number of wrong guesses left.
If the user doesn't win, tell them the answer.
"""
import random

correct = []  # fill list with correct letters
# correct_string = ''
incorrect = []  # fill list with incorrect letters
# incorrect_string = ''
lower_case_hard_words = [hard_word.lower() for hard_word in hard_words]
# convert all to lower case too


def word_game():
    correct_string = ''
    incorrect_string = ''

    # choose random word
    combined_words = words + lower_case_hard_words
    random_word = random.choice(combined_words)
    # print(f"random word is:___ {random_word}")
    length_of_word = len(random_word)
    # replace word with underscores for length of word
    word_replace_underscore = '_ ' * length_of_word
    print(f"this word is {length_of_word} letters long ....{word_replace_underscore}")

    # allow for 6 guesses
    for num in range(6):
        num_guesses_used = num+1
        guess = input("guess one letter:    >>   ")
        print(f"the guess is {guess}")
        if guess not in random_word:
            print(f" that letter: {guess} is NOT the word ....")
            # incorrect.append(guess)
            incorrect_string += guess
        else:
            print(f" that letter: {guess} IS INDEED in the word")
            # correct.append(guess)
            correct_string += guess
            print(f"NUM HERE IS {num}")
        print(f"your WRONG guesses so far {incorrect_string}")
        print(f"your CORRECT guesses so far CORRECT STRING {correct_string}")
        print(f"number guesses used {num + 1}")

        if num_guesses_used == 6:
            guess_word = input("do you want to guess the word?:   >>   ")
            if guess_word == random_word:
                print(f"you won!! that is correct")
            else:
                print(f"sorry, that is not correct, the word was: {random_word}")

                
word_game()
