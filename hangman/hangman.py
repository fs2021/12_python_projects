import random
import string
from words import wordslist
#print (wordslist[random.randint(0, len(wordslist))])

def get_valid_word(wordslist):
    word = random.choice(wordslist)
    while '-' in word or ' ' in word:
        word = random.choice(wordslist)

    return word.upper()

def hangman():
    word = get_valid_word(wordslist)
    word_letters = set(word) #letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what user has guessed
    count = 0
    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print("You have used these letters: ", " ".join(used_letters))
        #" ".join(['a', 'b', 'cd']) --> 'a b cd'

        #what current word is (ie W-RD)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print ("Current word: ", ' '.join(word_list))


        user_letter = input("Guess a letter: ").upper()
        count = count + 1
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else: 
                lives = lives - 1
                print ("Letter is wrong, ", lives, " left.")    
        elif user_letter in used_letters:
            print("you have used it")
        else:
            print("invalid character") 

    if lives == 0:
        print("You died.")
    print(f"word is: {word}, you made {count} attempts.")

hangman()


