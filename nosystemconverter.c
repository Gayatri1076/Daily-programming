#include <stdio.h>

void decimalToBinary(int n) {
    int binary[32], i = 0;

    while (n > 0) {
        binary[i++] = n % 2;
        n /= 2;
    }

    printf("Binary: ");
    for (int j = i - 1; j >= 0; j--)
        printf("%d", binary[j]);
    printf("\n");
}

int main() {
    int number, choice;

    printf("===== NUMBER SYSTEM CONVERTER =====\n");

    printf("Enter Decimal Number: ");
    scanf("%d", &number);

    printf("\n1. Binary\n");
    printf("2. Octal\n");
    printf("3. Hexadecimal\n");
    printf("Choose Option: ");
    scanf("%d", &choice);

    switch(choice) {

        case 1:
            decimalToBinary(number);
            break;

        case 2:
            printf("Octal: %o\n", number);
            break;

        case 3:
            printf("Hexadecimal: %X\n", number);
            break;

        default:
            printf("Invalid Choice!");
    }

    return 0;
}