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


def pick_random_word():
    lower_case_hard_words = [hard_word.lower() for hard_word in hard_words]
    random_word_answer = random.choice(lower_case_hard_words)
    return random_word_answer


class HangmanGame(object):
    def __init__(self):
        self.number_of_guesses_allowed = 6
        self.guessed_letters_list = []
        self.player_answer_so_far = ''
        self.random_answer = pick_random_word()

    def play_the_game(self):
        while self.number_of_guesses_allowed > 0:
            print(f"number guesses {self.number_of_guesses_allowed}, random word {self.random_answer}")
            guessed_letter = input("Guess a letter: >>>   ")
            self.guessed_letters_list.append(guessed_letter)
            self.player_answer_so_far = ''
            for letter in self.random_answer:
                if letter in self.guessed_letters_list:
                    # print(f"guessed letters list: {guessed_letters_list}")
                    self.player_answer_so_far += letter
                else:
                    self.player_answer_so_far += "_"

            # print(f"player_answer_so_far: {self.player_answer_so_far}")
            # guessed_letter = input("Guess a letter: >>>   ")
            # self.guessed_letters_list.append(guessed_letter)
            print(f"your letter guesses so far:  {self.guessed_letters_list}")
            print(f"player_answer_so_far: {self.player_answer_so_far}")

            if self.player_answer_so_far == self.random_answer:
                print(f"you win word is {self.random_answer}")
                break
            if guessed_letter in self.random_answer:
                print(f"Yes!!!! correct, that letter is in the word{self.number_of_guesses_allowed}")
            else:
                self.number_of_guesses_allowed -= 1  # decrease guesses if wrong
                print(f"Sorry!!! NO,  try another guess, number guesses left: ..... {self.number_of_guesses_allowed}")

            if self.number_of_guesses_allowed == 1:
                guessed_word = input("Would you like to guess the word? >>>  ")
                print
                if guessed_word == self.random_answer:
                    print("You won!")
                    return
                else:
                    print(f"sorry, you lost :( the word was {self.random_answer}")
                    return
        # guessed_letter = input("Guess a letter: >>>   ")
        # self.guessed_letters_list.append(guessed_letter)
        # print(f"your letter guesses so far:  {self.guessed_letters_list}")

        # if guessed_letter in self.random_answer:
        #     print(f"Yes!!!! correct, that letter is in the word{self.number_of_guesses_allowed}")
        # else:
        #     self.number_of_guesses_allowed -= 1  # decrease guesses if wrong
        #     print(f"Sorry!!! NO,  try another guess, number guesses left: ..... {self.number_of_guesses_allowed}")
        #
        # if self.number_of_guesses_allowed == 1:
        #     guessed_word = input("Would you like to guess the word? >>>  ")
        #     print
        #     if guessed_word == self.random_answer:
        #         print("You won!")
        #         return
        #     else:
        #         print(f"sorry, you lost :( the word was {self.random_answer}")
        #         return


if __name__ == "__main__":
    game = HangmanGame()
    game.play_the_game()


