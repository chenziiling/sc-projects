"""
File: hangman.py
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
to try in order to win this game.
"""


import random


# This constant controls the number of guess the player has
N_TURNS = 7


def main():
    """
    This program is a game. Player has to guess a random word in limited chances.
    """
    ans = random_word()
    on_screen = ''
    chance = N_TURNS
    for i in range(len(ans)):
        on_screen += '-'
    print('The word looks like: ' + on_screen)
    print('You have ' + str(chance) + ' guesses left.')
    # be ready to start the game
    while True:
        # break when the user wins or loses
        guess = input('Your guess: ')
        guess = guess.upper()
        if guess.isalpha() and len(guess) == 1:
            if is_right_guess(ans, guess):
                # user's guess is in the answer
                on_screen = change_on_screen(ans, guess, on_screen)
                print('You are correct!')
                if on_screen == ans:
                    print('You win!!!')
                    print('The word was: ' + ans)
                    break
                print('The word looks like: ' + on_screen)
                print('You have ' + str(chance) + ' guesses left.')
            else:
                # user's guess isn't in the answer
                print('There\'s no ' + guess + '\'s in the word.')
                print('The word looks like: ' + on_screen)
                chance -= 1
                if chance == 0:
                    print('You are completely hung:(')
                    print('The word was: ' + ans)
                    break
                print('You have ' + str(chance) + ' guesses left.')
        else:
            # user's guess isn't an alpha or the guess is over one letter
            print('illegal format.')
            chance -= 1
            if chance == 0:
                print('You are completely hung:(')
                print('The word was: ' + ans)
                break
            print('You have ' + str(chance) + ' guesses left.')


def is_right_guess(ans, guess):
    """
    :param ans: string,the answer to this game
    :param guess: char,user's guess
    :return: if the guess is in the answer,return true,if not,return false
    """
    for ch in ans:
        if guess == ch:
            return True
    return False


def change_on_screen(ans, guess, on_screen):
    """
    :param ans: string,the answer to this game
    :param guess: char,user's guess
    :param on_screen: string,previous status
    :return: the updated status
    """
    new_on_screen = ''
    for i in range(len(ans)):
        if on_screen[i].isalpha():
            new_on_screen += on_screen[i]
        elif ans[i] == guess:
            new_on_screen += guess
        else:
            new_on_screen += '-'
    return new_on_screen


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
