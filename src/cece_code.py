"""
Final Project Cecelia and Ellie
main code
12/5/24
CS1210A
"""
import time
import wagner_fischer
import random

TEST_PHRASE = [
                "The quick brown fox jumps over the lazy dog.",
                "Don’t put all your eggs in one basket.",
                "One small step for man, one giant leap for mankind - Neil Armstrong 1969",
                "Tongue Twister: She sells sea shells by the sea shore",
                "I scream, you scream, we all scream for icecream",
                "...and a partridge in a pear tree."
            ]
TEST_CODING = [
                'if __name__ == "__main__":',
                "public static void main (String[] args) {",
                'print("Hello, World!")'
            ]


def play(TEST):
    start = time.time()

    user = input(f"Start Typing: {TEST} \n")

    end = time.time()
    difference = end - start

    errors = wagner_fischer.distance(user, TEST)
    print(f"It took you {difference:.2f} seconds")
    print(f"You made {errors} errors.")
    print(f"Your accuracy was {100 - (errors/len(TEST)):.2%}")


if __name__ == "__main__":
    while True:
        uchoice = input("Welcome to Typing Test. Type `p` to test with a phrase,"
                        "`c` to test with code, and `e` to End: ")

        if uchoice == "p":
            play(random.choice(TEST_PHRASE))

        elif uchoice == "c":
            play(random.choice(TEST_CODING))

        elif uchoice == "e":
            print("Thank you for playing.")
            break

        else:
            uchoice = input("That is not a correct input. Type `p` to test with a phrase,"
                            "`c` to test with code, and `e` to End: ")