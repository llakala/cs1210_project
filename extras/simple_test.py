errors = 0

phrase = "hello"
attempt = "hello"

length = len(phrase)
difference = abs(len(attempt) - len(phrase))

for index in range(length):
    phrase_char = phrase[index]
    attempt_char = attempt[index]

    if phrase_char != attempt_char:
        errors += 1

errors += difference

print(errors)
