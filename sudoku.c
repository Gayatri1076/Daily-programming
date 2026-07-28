#include <stdio.h>

int main() {
    int grid[9][9];
    int valid = 1;

    printf("Enter 9x9 Sudoku Grid:\n");

    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            scanf("%d", &grid[i][j]);
        }
    }

    // Check rows
    for (int i = 0; i < 9; i++) {
        int seen[10] = {0};

        for (int j = 0; j < 9; j++) {
            int num = grid[i][j];

            if (num < 1 || num > 9 || seen[num]) {
                valid = 0;
                break;
            }

            seen[num] = 1;
        }

        if (!valid)
            break;
    }

    if (valid)
        printf("\nRows are Valid.\n");
    else
        printf("\nInvalid Sudoku Row!\n");

    return 0;
}