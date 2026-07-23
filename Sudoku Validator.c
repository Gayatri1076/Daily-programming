#include <stdio.h>

int main() {
    int sudoku[9][9];
    int i, j, k;

    printf("Enter 9x9 Sudoku Matrix:\n");

    for(i = 0; i < 9; i++) {
        for(j = 0; j < 9; j++) {
            scanf("%d", &sudoku[i][j]);
        }
    }

    // Check Rows
    for(i = 0; i < 9; i++) {
        int visited[10] = {0};

        for(j = 0; j < 9; j++) {
            if(sudoku[i][j] < 1 || sudoku[i][j] > 9 || visited[sudoku[i][j]]) {
                printf("Invalid Sudoku\n");
                return 0;
            }
            visited[sudoku[i][j]] = 1;
        }
    }

    // Check Columns
    for(j = 0; j < 9; j++) {
        int visited[10] = {0};

        for(i = 0; i < 9; i++) {
            if(visited[sudoku[i][j]]) {
                printf("Invalid Sudoku\n");
                return 0;
            }
            visited[sudoku[i][j]] = 1;
        }
    }

    printf("Valid Sudoku (Rows & Columns)\n");

    return 0;
}