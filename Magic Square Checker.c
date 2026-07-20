#include <stdio.h>

int main() {
    int a[3][3];
    int i, j;
    int sum, flag = 1;

    printf("Enter 3x3 Matrix:\n");

    for(i = 0; i < 3; i++)
        for(j = 0; j < 3; j++)
            scanf("%d", &a[i][j]);

    sum = a[0][0] + a[0][1] + a[0][2];

    // Check rows
    for(i = 1; i < 3; i++) {
        if(a[i][0] + a[i][1] + a[i][2] != sum)
            flag = 0;
    }

    // Check columns
    for(j = 0; j < 3; j++) {
        if(a[0][j] + a[1][j] + a[2][j] != sum)
            flag = 0;
    }

    // Check diagonals
    if(a[0][0] + a[1][1] + a[2][2] != sum)
        flag = 0;

    if(a[0][2] + a[1][1] + a[2][0] != sum)
        flag = 0;

    if(flag)
        printf("Magic Square");
    else
        printf("Not a Magic Square");

    return 0;
}