#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main() {
    char password[100];
    int upper = 0, lower = 0, digit = 0, special = 0;

    printf("Enter Password: ");
    scanf("%s", password);

    int len = strlen(password);

    for (int i = 0; i < len; i++) {
        if (isupper(password[i]))
            upper = 1;
        else if (islower(password[i]))
            lower = 1;
        else if (isdigit(password[i]))
            digit = 1;
        else
            special = 1;
    }

    printf("\nPassword Analysis\n");
    printf("-----------------\n");

    if (len >= 8 && upper && lower && digit && special)
        printf("Strong Password ✅\n");
    else
        printf("Weak Password ❌\n");

    return 0;
}