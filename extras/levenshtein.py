def levenshteinRecursive(str1, str2):
    len1 = len(str1)
    len2 = len(str2)

    # str1 is empty
    if len1 == 0:
        return len2

    # str2 is empty
    if len2 == 0:
        return len1

    head1 = str1[0]  # First character of str1
    head2 = str2[0]  # First character of str2
    headless1 = str1[1:]  # str1 without its first character
    headless2 = str2[1:]  # str2 without its first character

    if head1 == head2:
        return levenshteinRecursive(headless1, headless2)

    insert = levenshteinRecursive(str1, headless2)
    remove = levenshteinRecursive(headless1, str2)
    replace = levenshteinRecursive(headless1, headless2)
    return 1 + min(insert, remove, replace)

# Drivers code


str1 = "Hi there bobby johnson, you are awesome."
str2 = "Hi there bobby johnson, you are great. I miss"

distance = levenshteinRecursive(str1, str2)
print("Levenshtein Distance:", distance)
