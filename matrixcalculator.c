#include <stdio.h>

int main() {
    int r1, c1, r2, c2;
    int A[10][10], B[10][10], R[10][10];
    int choice;

    printf("===== MATRIX CALCULATOR =====\n");

    printf("Enter rows and columns of Matrix A: ");
    scanf("%d %d", &r1, &c1);

    printf("Enter rows and columns of Matrix B: ");
    scanf("%d %d", &r2, &c2);

    printf("\nEnter Matrix A:\n");
    for(int i = 0; i < r1; i++)
        for(int j = 0; j < c1; j++)
            scanf("%d", &A[i][j]);

    printf("\nEnter Matrix B:\n");
    for(int i = 0; i < r2; i++)
        for(int j = 0; j < c2; j++)
            scanf("%d", &B[i][j]);

    printf("\n1. Addition");
    printf("\n2. Subtraction");
    printf("\n3. Multiplication");
    printf("\nChoose Operation: ");
    scanf("%d", &choice);

    switch(choice) {

    case 1:
        if(r1 != r2 || c1 != c2) {
            printf("Addition Not Possible!");
            break;
        }

        printf("\nResult:\n");
        for(int i = 0; i < r1; i++) {
            for(int j = 0; j < c1; j++) {
                R[i][j] = A[i][j] + B[i][j];
                printf("%4d", R[i][j]);
            }
            printf("\n");
        }
        break;

    case 2:
        if(r1 != r2 || c1 != c2) {
            printf("Subtraction Not Possible!");
            break;
        }

        printf("\nResult:\n");
        for(int i = 0; i < r1; i++) {
            for(int j = 0; j < c1; j++) {
                R[i][j] = A[i][j] - B[i][j];
                printf("%4d", R[i][j]);
            }
            printf("\n");
        }
        break;

    case 3:
        if(c1 != r2) {
            printf("Multiplication Not Possible!");
            break;
        }

        printf("\nResult:\n");
        for(int i = 0; i < r1; i++) {
            for(int j = 0; j < c2; j++) {
                R[i][j] = 0;
                for(int k = 0; k < c1; k++)
                    R[i][j] += A[i][k] * B[k][j];

                printf("%4d", R[i][j]);
            }
            printf("\n");
        }
        break;

    default:
        printf("Invalid Choice!");
    }

    return 0;
}