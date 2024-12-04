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
                "I scream, you scream, we all scream for ice cream",
                "...and a partridge in a pear tree.",
                "I before E, except after C, or when sounding like A",
                "Shall I compare thee to a summer's day?",
                "To be or not to be, that is the question."
            ]
TEXT_CODE = [
                'if __name__ == "__main__":',
                "public static void main (String[] args) {",
                'print("Hello, World!")',
                'environment.systemPackages = with pkgs;',
                "avg = sum(lst) / len(lst)",
                'print(f"Your lucky number is {random.random():.2f}!")'
            ]

def play(PROMPT):
    start = time.time()
    attempt = input(f"Start Typing: \n{PROMPT}\n")
    end = time.time()

    difference = end - start

    errors = wagner_fischer.distance(attempt, PROMPT)
    if errors > len(PROMPT):
        errors = len(PROMPT)

    inaccuracy = errors / len(PROMPT)
    accuracy = 1 - inaccuracy

    words = len(attempt.split(" "))
    per_minute = 60 / difference

    wpm = words * per_minute

    print(f"You typed {words} words in {difference:.2f} seconds.")
    print(f"This gives you a WPM of {wpm:.2f}")
    print()
    print(f"Your accuracy was {accuracy * 100:.2f}%")
    print(f"Accounting for errors, your true WPM was {(wpm * accuracy).2f}")


if __name__ == "__main__":
    print("Welcome to Typing Test. ")
    while True:
        uchoice = input("Type 'A' to test with a phrase, "
                        "'B' to test with code, and 'X' to End: ")
        uchoice = uchoice.strip()
        if uchoice == 'A':
            play(random.choice(TEXT_PHRASES))
        elif uchoice == 'B':
            play(random.choice(TEXT_CODE))
        elif uchoice == 'X':
            print("Thank you for playing.")
            break
        else:
            print("That is not correct input.")
