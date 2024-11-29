# Return a 2d array
def empty2d(columns, rows):
    matrix = []
    baseRow = [0] * columns

    for i in range(rows):
        row = baseRow.copy()
        matrix.append(row)

    return matrix


def distance(str1, str2):
    cols = len(str1) + 1
    rows = len(str2) + 1

    matrix = empty2d(cols, rows)

    # First row stores lengths of str1
    for col in range(cols):
        matrix[0][col] = col

    # First column stores lengths of str2
    for row in range(rows):
        matrix[row][0] = row

    for col in range(1, cols):
        for row in range(1, rows):
            above = matrix[row - 1][col]
            left = matrix[row][col - 1]
            corner = matrix[row - 1][col - 1]

            current1 = str1[col - 1]
            current2 = str2[row - 1]
            if current1 == current2:  # If the compared character is the same
                matrix[row][col] = min(above, left, corner)

            elif above == left:  # Substitution
                matrix[row][col] = 1 + corner

            else:  # Deletion or insertion
                matrix[row][col] = 1 + min(above, left, corner)

    # for row in matrix:
    #     print(row)

    return matrix[-1][-1]


str1 = ""
str2 = ""
output = distance(str1, str2)
print(output)
