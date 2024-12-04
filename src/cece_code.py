"""
Final Project Cecelia and Ellie
main code
12/5/24
CS1210A
"""
import time
import wagner_fischer
import random

TEXT_PHRASES = [
                "The quick brown fox jumps over the lazy dog.",
                "Don’t put all your eggs in one basket.",
                "One small step for man, one giant leap for mankind - Neil Armstrong 1969",
                "Tongue Twister: She sells sea shells by the sea shore",
                "I scream, you scream, we all scream for icecream",
                "...and a partridge in a pear tree."
            ]
TEXT_CODE = [
                'if __name__ == "__main__":',
                "public static void main (String[] args) {",
                'print("Hello, World!")'
            ]


def play(PROMPT):
    start = time.time()
    attempt = input(f"Start Typing: \n{PROMPT}\n")
    end = time.time()

    difference = end - start

    errors = wagner_fischer.distance(attempt, PROMPT)
    percentage_wrong = 100 * (errors / len(PROMPT))

    print(f"It took you {difference:.2f} seconds")
    print(f"You made {errors} errors.")
    print(f"Your accuracy was {100 - percentage_wrong:.2f}%")


if __name__ == "__main__":
    while True:
        uchoice = input("Welcome to Typing Test. Type 'A' to test with a phrase,"
                    "'B' to test with code, and 'X' to End: ")
        if uchoice == 'A':
            play(random.choice(TESTPHRASE))
        elif uchoice == 'B':
            play(random.choice(TESTCODING))
        elif uchoice == 'X':
            print("Thank you for playing.")
            break
        else:
            uchoice = input("That is not a correct input. "
                            "Type `p` to test with a phrase, "
                            "`c` to test with code, and `e` to End: ")
