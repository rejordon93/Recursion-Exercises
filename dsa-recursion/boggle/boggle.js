function find(board, word) {
  // Helper function to explore adjacent cells in NEWS directions
  function explore(row, col, index) {
    // Base case: If we've reached the end of the word, return true
    if (index === word.length) {
      return true;
    }

    // Check if the current cell is out of bounds or doesn't match the current letter
    if (
      row < 0 ||
      col < 0 ||
      row >= board.length ||
      col >= board[0].length ||
      board[row][col] !== word[index]
    ) {
      return false;
    }

    // Temporarily mark the current cell as visited
    const temp = board[row][col];
    board[row][col] = "*";

    // Explore all four NEWS directions recursively
    const found =
      explore(row - 1, col, index + 1) ||
      explore(row + 1, col, index + 1) ||
      explore(row, col - 1, index + 1) ||
      explore(row, col + 1, index + 1);

    // Restore the original value of the cell
    board[row][col] = temp;

    return found;
  }

  // Iterate over each cell in the board and start the search from there
  for (let row = 0; row < board.length; row++) {
    for (let col = 0; col < board[0].length; col++) {
      if (board[row][col] === word[0] && explore(row, col, 0)) {
        return true;
      }
    }
  }

  return false; // Word not found on the board
}

// EXAMPLE TEST
const board = makeBoard(`N C A N E
                         O U I O P
                         Z Q Z O N
                         F A D P L
                         E D E A Z`);

console.log(find(board, "NOON"), true); // Output: true
console.log(find(board, "NOPE"), true); // Output: true
console.log(find(board, "CANON"), false); // Output: false
console.log(find(board, "QUINE"), false); // Output: false
console.log(find(board, "FADED"), true); // Output: true

const board2 = makeBoard(`E D O S Z
                          N S O N R
                          O U O O P
                          Z Q Z O R
                          F A D P L`);

console.log(find(board2, "NOOOOS"), true); // Output: true
