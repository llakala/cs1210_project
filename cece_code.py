import time

TEST = 'The quick brown fox jumps over the lazy dog.'

start = time.time()
user = input(f"Start Typing: {TEST} \n")
end = time.time()
difference = end - start

print(f"It took you {difference:.2f} seconds")

errors = abs(len(TEST) - len(user))

for i, l in enumerate(TEST):
    if user[i] != l:
        errors += 1

print(f"You made {errors} errors.")