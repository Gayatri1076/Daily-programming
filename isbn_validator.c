#include <stdio.h>
#include <string.h>

int main() {
    char isbn[11];
    int sum = 0;

    printf("Enter ISBN-10 (10 digits): ");
    scanf("%10s", isbn);

    if (strlen(isbn) != 10) {
        printf("Invalid ISBN Length!\n");
        return 0;
    }

    for (int i = 0; i < 10; i++) {
        if (isbn[i] < '0' || isbn[i] > '9') {
            printf("Invalid ISBN! Only digits allowed.\n");
            return 0;
        }

        sum += (isbn[i] - '0') * (10 - i);
    }

    if (sum % 11 == 0)
        printf("Valid ISBN-10\n");
    else
        printf("Invalid ISBN-10\n");

    return 0;
}