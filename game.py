import json
import re
import random
import string
import inquirer

def hangman(choice):
    if choice == 'Film':
        word_file = open('movies.json').read()
    elif choice == 'Animals':
        word_file = open('animals.json').read()
    elif choice == 'Country':
        word_file = open('countries.json').read()
    else:
        word_file = open('words.json').read()

    words = json.loads(word_file)

    word = random.choice(words).upper()
    word_letters = set(re.sub('[^A-Za-z0-9]+', '', word))

    used_letters = set()

    alphabet = set(string.ascii_uppercase)

    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print('\nYou have', lives, 'lives and you have used these letters:', ''.join(used_letters))

        word_list = []

        for letter in word:
            if letter in used_letters:
                word_list.append(letter)
            elif letter == ':' or letter == ' ' or letter.isalpha() == False:
                word_list.append(letter)
            else:
                word_list.append('_')

        print('\nCurrent', choice ,':', ''.join(word_list), '\n')

        letter = input('Guess a letter: ').upper()

        if letter in alphabet - used_letters:
            used_letters.add(letter)

            if letter in word_letters:
                word_letters.remove(letter)
            else:
                lives -= 1
                print('\nSorry, that\'s not in the answer.')

        elif letter in used_letters:
            print('\nYou\'ve already used that letter you div\n')

        else:
            print('\nAre you stupid? That\'s not a letter!')

    if lives == 0:
        print('\n=============================')
        print('\nHahahaha! You fucking loser. It\'s over. You\'re out of lives. The', choice.lower(), 'was', word)
        print('\n=============================')
    else:
        print('\n=============================')
        print('\nYou win! You guessed the', choice.lower(), ':', word)
        print('\n=============================')


questions =[
    inquirer.List('topic', message='Choose a topic', choices=['Animals', 'Country', 'Film', 'Random Word'])
]

answers = inquirer.prompt(questions)

hangman(answers['topic'])