#include <stdio.h>

// Function to print the Tic-Tac-Toe board
void printBoard(char board[3][3]) {
    printf("\n  A B C\n");
    for (int i = 0; i < 3; ++i) {
        printf("%d ", i + 1);
        for (int j = 0; j < 3; ++j) {
            printf("%c", board[i][j]);
            if (j < 2) printf("|");
        }
        printf("\n");
        if (i < 2) printf("  -----\n");
    }
    printf("\n");
}

// Function to check if a player has won
int checkWin(char board[3][3], char player) {
    // Check rows and columns
    for (int i = 0; i < 3; ++i) {
        if ((board[i][0] == player && board[i][1] == player && board[i][2] == player) ||
            (board[0][i] == player && board[1][i] == player && board[2][i] == player))
            return 1;
    }

    // Check diagonals
    if ((board[0][0] == player && board[1][1] == player && board[2][2] == player) ||
        (board[0][2] == player && board[1][1] == player && board[2][0] == player))
        return 1;

    return 0;
}

// Function to check if the board is full (tie)
int checkTie(char board[3][3]) {
    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
            if (board[i][j] == ' ') {
                return 0; // There's an empty space, game is not a tie
            }
        }
    }
    return 1; // Board is full, game is a tie
}

int main() {
    char board[3][3] = {{' ', ' ', ' '}, {' ', ' ', ' '}, {' ', ' ', ' '}};
    int row, col;
    char currentPlayer = 'X';
    int gameOver = 0;

    printf("Welcome to Tic-Tac-Toe!\n");

    do {
        printBoard(board);

        // Get player move
        do {
            printf("Player %c, enter your move (row column): ", currentPlayer);
            if (scanf("%d %d", &row, &col) != 2 || row < 1 || row > 3 || col < 1 || col > 3 || board[row - 1][col - 1] != ' ') {
                printf("Invalid move. Try again.\n");
                while (getchar() != '\n'); // Clear input buffer
            } else {
                break;
            }
        } while (1);

        // Update board
        board[row - 1][col - 1] = currentPlayer;

        // Check for win or tie
        if (checkWin(board, currentPlayer)) {
            printBoard(board);
            printf("Player %c wins! Game over.\n", currentPlayer);
            gameOver = 1;
        } else if (checkTie(board)) {
            printBoard(board);
            printf("It's a tie! Game over.\n");
            gameOver = 1;
        }

        // Switch player for the next turn
        currentPlayer = (currentPlayer == 'X') ? 'O' : 'X';

    } while (!gameOver);

    return 0;
}
