def find(board, word):
    def dfs(row, col, index):
        if index == len(word):
            return True

        # Check if the current cell is out of bounds or doesn't match the current letter
        if (
            row < 0
            or col < 0
            or row >= 5
            or col >= 5
            or board[row][col] != word[index]
        ):
            return False

        # Temporarily mark the current cell as visited
        temp = board[row][col]
        board[row][col] = "*"

        # Explore all possible neighboring cells
        found = (
            dfs(row - 1, col, index + 1)
            or dfs(row + 1, col, index + 1)
            or dfs(row, col - 1, index + 1)
            or dfs(row, col + 1, index + 1)
        )

        # Restore the original value of the cell
        board[row][col] = temp

        return found

    # Iterate over all cells to start the search
    for row in range(5):
        for col in range(5):
            if board[row][col] == word[0] and dfs(row, col, 0):
                return True

    return False

# Test cases
board = make_board('''
N C A N E
O U I O P
Z Q Z O N
F A D P L
E D E A Z
''')

print(find(board, "NOON"))   # Output: True
print(find(board, "NOPE"))   # Output: True
print(find(board, "CANON"))  # Output: False
print(find(board, "QUINE"))  # Output: False
print(find(board, "FADED"))  # Output: True

board2 = make_board('''
E D O S Z
N S O N R
O U O O P
Z Q Z O R
F A D P L
''')

print(find(board2, "NOOOOS"))  # Output: True
