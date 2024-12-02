# Return a 2d array
def empty2d(columns, rows):
    matrix = []
    baseRow = [0] * columns

    for i in range(rows):
        row = baseRow.copy()
        matrix.append(row)

    return matrix


def distance(str1, str2):
    # Add one for a blank row at the left and top
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
            corner = matrix[row - 1][col - 1]  # Price to substitute
            above = matrix[row - 1][col]  # Price to add
            left = matrix[row][col - 1]  # Price to delete

            current1 = str1[col - 1]
            current2 = str2[row - 1]

            # If the new character is the same, the price to substitute is zero
            if current1 == current2:
                corner -= 1

            matrix[row][col] = 1 + min(above, left, corner)

    return matrix[-1][-1]
