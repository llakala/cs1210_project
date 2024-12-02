import time
import wagner_fischer

TEST = 'The quick brown fox jumps over the lazy dog.'

start = time.time()
user = input(f"Start Typing: {TEST} \n")
end = time.time()
difference = end - start

print(f"It took you {difference:.2f} seconds")

errors = wagner_fischer.distance(user, TEST)

print(f"You made {errors} errors.")
