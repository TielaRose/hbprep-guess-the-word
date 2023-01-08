####################################################
#GUESS THE WORD GAME
####################################################

####################################################
#TO DO
####################################################
# add feature to guess the whole word at once
# allow users to choose how many guesses they get
# hints?
# add comments to explain what's happening in the code

####################################################
#IMPORT
####################################################

import random
import replit
import time
from termcolor import cprint
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

def solution_to_list_of_blanks(word):
    """changes the solution word to an array of blank spaces (two spaces per letter in the solution word)"""
    output = []

    for let in word:
        output.append('__')

    return output

def print_box(str):
    """Print a box around a string"""
    box_width = len(str) + 2
    
    # create each line
    line1 = f'╔{"═" * box_width}╗'
    line2 = f'║{" " * box_width}║'
    line3 = f'║ {str} ║'
    line4 = line2
    line5 = f'╚{"═" * box_width}╝'

    # print each line
    cprint(line1, 'blue')
    cprint(line2, 'blue')
    cprint(line3, 'blue')
    cprint(line4, 'blue')
    cprint(line5, 'blue')

def list_to_string(list):
    """changes the list to a string"""
    output_string = ""
    
    for x in list:
        output_string = output_string + x + " "

    return output_string

def ask_for_letter(right_guesses, wrong_guesses):
    """asks the user to guess a letter"""
    while True:
        print()
        print('Guess a letter')
        letter_guessed = input('> ')

        # validate input: if it's one letter, move on
        if letter_guessed.isalpha() and len(letter_guessed) == 1:
            letter_guessed = letter_guessed.lower()
            if (letter_guessed in right_guesses) or (letter_guessed in wrong_guesses) :
                print(f'You have already guessed {letter_guessed.lower()}. Try a different letter')
            else:
                break
        # if it's more than one letter, give an error message
        elif letter_guessed.isalpha():
            print("Too many characters. Please enter ONE letter only")
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

def play_guess_the_word():

    play_game = True
    
    while play_game:
        #pick a random word to be the solution
        solution = gen_rand_word()
        
        #create a list of blanks for each letter in the solution
        display_list = solution_to_list_of_blanks(solution)
        
        won = False
        lost = False
        chances_left = 7
        wrong_letters = []
        delay = 2
        
        while not lost and not won:
            #greet the user, explain the rules
            greet_user()
            print_game_rules()
            
            #print the display word (blank spaces/guesses) to the console
            display_string = ' '.join(display_list)
            print_box(display_string)
    
            #print the letters guessed that are not in the word, if there are any
            if len(wrong_letters) > 0:
                print()
                cprint('not in the word:', 'red')
                wrong_lets = list_to_string(wrong_letters)
                cprint(wrong_lets, 'red')
                print()
                if chances_left > 1:
                    cprint(f'chances left: {chances_left}', 'yellow')
                elif chances_left == 1:
                    cprint(f'chances left: {chances_left}', 'magenta')
        
            #ask the user to guess a letter
            letter_guessed = ask_for_letter(display_list, wrong_letters)
        
            #check if the letter guessed is in the word
            letter_guessed_in_word = is_letter_guessed_in_word(letter_guessed, solution)
        
            #if the letter guessed is not in the word, tell the user and display the letters guessed that aren't in the word, as well as the number of guesses left (maybe empty boxes?)
            if not letter_guessed_in_word:
                delay = 2
                update_wrong_guesses(wrong_letters, letter_guessed)
                chances_left -= 1
                cprint(f'"{letter_guessed}" is not in the word.', 'red')
                print()
                if chances_left > 1:
                    cprint(f'You have {chances_left} chances left.', 'yellow')
                elif chances_left == 1:
                    cprint('You only have one chance left!', 'magenta')
                print()
                
            # if the letter IS in the word, update the word
            elif letter_guessed_in_word:
                delay = 1
                indices = ind_of_letter(letter_guessed, solution)
                display_list = update_display(display_list, letter_guessed, indices)
                cprint(f'"{letter_guessed}" is in the word!', 'green')
                print()
                # check if the user has won
                if check_win(display_list):
                    cprint("Congratulations, you won!", 'blue')
                    print()
                    cprint(f'The word was: {solution}', 'blue')
                    won = True
        
            if chances_left == 0:
                print('So sorry, you lost!')
                print()
                print(f'The word was: {solution}')
                lost = True
    
            if not lost and not won:
                time.sleep(1)
                replit.clear()
    
        if won or lost:
            print()
            print('Would you like to play again? Y/N')
    
            while True:
                play_again = input("> ").upper()
        
                if play_again == 'Y':
                    #pick a random word to be the solution
                    solution = gen_rand_word()
            
                    #create a list of blanks for each letter in the solution
                    display_list = solution_to_list_of_blanks(solution)
                    won = False
                    lost = False
                    chances_left = 7
                    wrong_letters = []
                    delay = 2
    
                    time.sleep(delay)
                    replit.clear()
                    
                    break
                elif play_again == 'N':
                    print()
                    print('Thanks for playing - goodbye!')
                    play_game = False
                    break
                else:
                    print('Invalid input. Please enter "Y" or "N"')



play_guess_the_word()