# Hangman in Pyhton

from wordslist import words
import random
#words = ("apple", "orange", "banana", "coconut", "pineapple")
#if you would like to import a larger variety of words. we could create a seperate python file for that


#dictionary of key:()
hangman_art = {0:("  ",
                  "  ",
                  "  "),
               1:(" o ",
                  "  ",
                  "  "),
               2:(" o ",
                  " | ",
                  "  "),
               3:(" o ",
                  "/| ",
                  "  "),
               4:(" o ",
                  "/|\\",
                  "  "),
               #if you use a backs slash that's an escape sequence within a string
               #you have to use double backs slashes, to literally print a backslash
               5:(" o ",
                  "/|\\",
                  "/  "),
               6:(" o ",
                  "/|\\",
                  "/ \\")}

#for line in hangman_art[6]:
#    print(line)

def display_man(wrong_guesses):
    print("***********")
    for line in hangman_art[wrong_guesses]:
    #for every line in my hangman_art add the key of wrong_guesses
        print(line)
    print("***********")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
#normally in pyhton you can't create an empty set with just a set of parentheses
#we have to use the set function
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha() :
            print("Invalid input")
            continue


        if guess in guessed_letters:
            print(f"{guess} is already guessed")

        guessed_letters.add(guess)


        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess

        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU WIN!")
            is_running = False
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU LOSE!")
            is_running = False


if __name__ == "__main__":
    main()
