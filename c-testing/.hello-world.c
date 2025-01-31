Sure, here's how you can translate your Python function to C:

```c
#include <stdio.h>

#define SIZE 3  // Adjust the size of the board

// Function to print the game board
void print_board(char board[SIZE][SIZE]) {
    printf("Current Board:\n");
    int cell_value = 1;
    
    // Loop through each row
    for (int i = 0; i < SIZE; i++) {
        char row_str[100] = "";  // Assuming the row won't be longer than 100 characters
        
        // Loop through each cell in the row
        for (int j = 0; j < SIZE; j++) {
            if (j > 0) {
                // Add space between cells
                sprintf(row_str + strlen(row_str), " ");
            }
            
            // Logic to determine if the cell should display a number or a symbol
            if (board[i][j] == ' ') {
                sprintf(row_str + strlen(row_str), "%d", cell_value);
            } else {
                sprintf(row_str + strlen(row_str), "%c", board[i][j]);
            }
            
            if (j < SIZE - 1) {
                // Add separator between cells
                sprintf(row_str + strlen(row_str), " |");
            }
            
            cell_value++;
        }
        
        printf("%s\n", row_str);  // Print the row
    }
}

int main() {
    // Example 3x3 game board with initial empty spaces
    char board[SIZE][SIZE] = {
        {' ', ' ', ' '},
        {' ', ' ', ' '},
        {' ', ' ', ' '}
    };

    print_board(board);
    return 0;
}
```

### Key Points:
1. **Board Definition**: A 2D array `board[SIZE][SIZE]` represents the board. I've defined `SIZE` as `3` here, but you can modify it for a different board size.
2. **Row Construction**: Instead of concatenating strings with `+=` (as in Python), we use `sprintf` in C to append formatted text to the `row_str` buffer.
3. **Looping Through the Board**: Nested loops are used to go through each row and column of the board. For each cell, we check if it's an empty space (`' '`) and print either a cell number or the character present.
4. **Printing**: The row is built up in `row_str` and printed after processing all the columns for that row.

This code assumes that the board will have an initial state with empty spaces `' '` and will increment `cell_value` across the rows, similar to your Python code.