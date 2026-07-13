#include <stdio.h>
#include <string.h>

int main() {
    char text[500], copy[500], search[50];
    int totalWords = 0, frequency = 0;

    printf("===== WORD FREQUENCY COUNTER =====\n");

    printf("Enter a sentence:\n");
    fgets(text, sizeof(text), stdin);

    strcpy(copy, text);

    printf("Enter the word to search: ");
    scanf("%s", search);

    char *token = strtok(copy, " \n");

    while (token != NULL) {
        totalWords++;

        if (strcmp(token, search) == 0)
            frequency++;

        token = strtok(NULL, " \n");
    }

    printf("\nTotal Words      : %d\n", totalWords);
    printf("'%s' Appears     : %d time(s)\n", search, frequency);

    return 0;
}