def levenshteinRecursive(str1, str2):
    len1 = len(str1)
    len2 = len(str2)

    # str1 is empty
    if len1 == 0:
        return len2

    # str2 is empty
    if len2 == 0:
        return len1

    tail1 = str1[-1]  # Last character of str1
    tail2 = str2[-1]  # Last character of str2
    siamese1 = str1[:-1]  # str1 without its last character
    siamese2 = str2[:-1]  # str2 without its last character

    if tail1 == tail2:
        return levenshteinRecursive(siamese1, siamese2)

    insert = levenshteinRecursive(str1, siamese2)
    remove = levenshteinRecursive(siamese1, str2)
    replace = levenshteinRecursive(siamese1, siamese2)
    return 1 + min(insert, remove, replace)

# Drivers code


str1 = "hello"
str2 = "bello"

distance = levenshteinRecursive(str1, str2)
print("Levenshtein Distance:", distance)
