// Adapted from Tic, Tac Toe created in Python
// https://github.com/Ethan-clay03/PoP/blob/main/week14/task1.py

#include <stdio.h>
#include <stdbool.h> 
#include <string.h>
#include <ctype.h>

#define SIZE 3 

char board[SIZE][SIZE] = {
    {' ', ' ', ' '},
    {' ', ' ', ' '},
    {' ', ' ', ' '}
};

void print_board(char board[SIZE][SIZE]);
int validate_input();
int check_valid_placement(int position);
char get_value_from_matrix(int position);
void set_value_in_matrix(int position_integer, int player);
char get_tile_icon(int player);
int get_row(int position_integer);
int get_col(int position_integer);
bool check_win(char player);
bool check_draw();

void play_game(int player) 
{
    printf("Player %d, it's your turn!\n", player);
    print_board(board);

    int player_input = validate_input();
    set_value_in_matrix(player_input, player);

    if (check_win(player)) {
        printf("Player %d won!\n", player);
        return;
    }

    if (check_draw()) {
        printf("The game ended in a tie! \n");
        return;
    }

    // Switch player
    player = (player == 1) ? 2 : 1;

    play_game(player);
}

void print_board(char board[SIZE][SIZE]) 
{
    printf("Current Board:\n");
    int cell_value = 1;

    for (int i = 0; i < SIZE; i++) {
        char row_str[100] = "";

        for (int j = 0; j < SIZE; j++) {
            if (j > 0) {
                sprintf(row_str + strlen(row_str), " ");
            }

            if (board[i][j] == ' ') {
                sprintf(row_str + strlen(row_str), "%d", cell_value);
            } else {
                sprintf(row_str + strlen(row_str), "%c", board[i][j]);
            }

            if (j < SIZE - 1) {
                sprintf(row_str + strlen(row_str), " |");
            }

            cell_value++;
        }

        printf("%s\n", row_str);
    }
}

int validate_input() 
{
    int player_selection;
    float user_input;
    bool valid_input = false;

    while (!valid_input) {
        printf("Enter the number tile you want to go in (1-9): ");
        
        if (scanf("%f", &user_input) != 1 || user_input != (int)user_input) {
            while (getchar() != '\n');
            printf("Invalid input! Please enter a valid number between 1 and 9.\n");
            continue;
        }
        
        player_selection = (int)user_input;

        if (player_selection < 1 || player_selection > 9) {
            printf("Invalid input! Please enter a number between 1 and 9. \n");
            continue;
        }

        if (!check_valid_placement(player_selection)) {
            printf("Sorry, that spot is already taken! Please choose a different spot. \n");
            continue;
        }

        valid_input = true;
    }

    return player_selection;
}

int check_valid_placement(int position) 
{
    return get_value_from_matrix(position) == ' ';
}

int get_row(int position_integer) 
{
    return (position_integer - 1) / SIZE;
}

int get_col(int position_integer) 
{
    return (position_integer - 1) % SIZE;
}

char get_value_from_matrix(int position_integer) 
{
    int row = get_row(position_integer);
    int col = get_col(position_integer);
    return board[row][col];
}

int main() {
    int player = 1;
    play_game(player);
    return 0;
}

void set_value_in_matrix(int position_integer, int player) 
{
    int row = get_row(position_integer);
    int col = get_col(position_integer);
    char value = get_tile_icon(player);
    
    board[row][col] = value;
}

char get_tile_icon(int player) 
{
    return player = (player == 1) ? 'X' : 'O';
}

bool check_win(char player) {
    for (int i = 0; i < SIZE; i++) {
        if (board[i][0] == board[i][1] && board[i][1] == board[i][2] && board[i][0] != ' ') {
            return true;
        }
        if (board[0][i] == board[1][i] && board[1][i] == board[2][i] && board[0][i] != ' ') {
            return true;
        }
    }

    if (board[0][0] == board[1][1] && board[1][1] == board[2][2] && board[0][0] != ' ') {
        return true;
    }
    if (board[0][2] == board[1][1] && board[1][1] == board[2][0] && board[0][2] != ' ') {
        return true;
    }

    return false;
}


bool check_draw() {
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            if (board[i][j] == ' ') {
                return false;
            }
        }
    }
    return true;
}