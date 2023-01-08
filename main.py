####################################################
#GUESS THE WORD GAME
####################################################

####################################################
#TO DO
####################################################
#finish game_rules() - if they know the word, can they guess the whole word? what is the consequence for guessing wrong?
#gen_rand_word() - maybe I should make my own list of words? Some of these words are terrible
#also filter out words with apostrophes
#validate input (make sure it's a letter, make sure it's only one letter)
#fix 2 chances/1 chance left thing
#allow the user to start the game again
#check if the user already guessed that letter
#use string.split() somewhere? instead of a loop?
#display: maybe display the wrong letters in red or something
#clear the console in between turns and just reprint the same stuff (so it's not super long)
    # can use import replit
    # replit.clear())

####################################################
#IMPORT
####################################################

import random
from word_list_file import word_list

####################################################
#FUNCTION DEFINITIONS
####################################################

def greet_user():
    """greets the user"""
    print("Welcome to 'Guess-the-Word'")
    

def print_game_rules():
    """explains the game rules/options"""
    game_rules = """
Try to guess the word before your chances run out!
Guess one letter at a time; if your letter is in 
the word, you're safe! But you only have 7 chances 
to get it wrong.

Good luck!
    """
    print(game_rules)

def gen_rand_word():
    """gets a random English word from a list of words"""
    solution_word = random.choice(word_list)

    return solution_word  

def solution_to_display(word):
    """changes the solution word to an array of blank spaces (one space per letter in the solution word)"""
    output = []

    for let in word:
        output.append('__')

    return output

def print_display(list):
    """prints a list to the console"""
    for x in list:
        print(f"{x} ", end = ' ')
    print()


def ask_for_letter():
    """asks the user to guess a letter"""
    while True:
        print()
        print('Guess a letter')
        letter_guessed = input('> ')
    
        if letter_guessed.isalpha():
            letter_guessed = letter_guessed.lower()
            break
        else:
            print("Invalid input. Please enter a letter only")
        print()

    return letter_guessed

def is_letter_guessed_in_word(letter, word):
    """checks if the letter guessed is in the solution word"""
    if letter in word:
        return True
    else:
        return False

def update_wrong_guesses(list, letter):
    """adds incorrectly guessed letters to the wrong guesses list """
    list.append(letter)
    return list

def ind_of_letter(letter, word):
    """returns the indices of each instances of a letter in a word"""
    indices = []

    for ind, let in enumerate(word):
        if let == letter:
            indices.append(ind)

    return indices

def update_display(list, letter, list_of_indices):
    """replaces blanks with the correct letter guessed"""
    for ind in list_of_indices:
        list[ind] = letter

    return list

def check_win(list):
    if '__' in list:
        return False
    else:
        return True
    

####################################################
#GAME PLAY
####################################################

#greet the user, explain the rules
greet_user()
print_game_rules()
    
#pick a random word to be the solution
solution = gen_rand_word()

#create an array of blanks for each letter in the solution
display = solution_to_display(solution)

play_game = True
win = False
chances_left = 7
wrong_letters = []

while play_game and not win:
    #print the display word (blank spaces) to the console
    print('The word is:')
    print_display(display)

    #ask the user to guess a letter
    letter_guessed = ask_for_letter()

    #check if the letter guessed is in the word
    letter_guessed_in_word = is_letter_guessed_in_word(letter_guessed, solution)

    #if the letter guessed is not in the word, tell the user and display the letters guessed that aren't in the word, as well as the number of guesses left (maybe empty boxes?)
    if not letter_guessed_in_word:
        update_wrong_guesses(wrong_letters, letter_guessed)
        chances_left -= 1
        print(f'"{letter_guessed}" is not in the word.')
        print()
        print(f'You have {chances_left} chance(s) left.')
        print()
        print('These letters are NOT in the word:')
        print_display(wrong_letters)
        print()
        
    # if the letter IS in the word, update the word
    elif letter_guessed_in_word:
        indices = ind_of_letter(letter_guessed, solution)
        display = update_display(display, letter_guessed, indices)
        print(f'"{letter_guessed}" is in the word!')
        print()
        # check if the user has won
        if check_win(display):
            print("Congratulations, you won!")
            print(f"The word was {solution}")
            win = False

    if chances_left == 0:
        print('So sorry, you lost!')
        print(f'The word was {solution}')
        play_game = False

# display the word/incorrect guesses
# prompt for another guess

# after ___ incorrect guesses, the user loses
# of if the user guesses the word, they win

# ask if they want to play again


# ####################################################
# #QUESTIONS
# ####################################################

# #am I making too many tiny little functions? Should I be combining some of these? I want to go towards "best practices" but I'm not sure what that is really or where the line is

# #single quotes vs double quotes: I can see myself switching back and forth which is no good. I can see the case for using double quotes always because then you can use an apostrophe and not have everything go crazy, but I also feel like when I see other people's code (on CodeWars and stuff) it seems like people generally use single quotes more often
