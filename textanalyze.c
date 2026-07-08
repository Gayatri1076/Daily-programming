#include <stdio.h>
#include <ctype.h>

int main() {
    char text[500];
    int characters = 0, words = 1, vowels = 0;
    int consonants = 0, digits = 0, spaces = 0;
    int special = 0;

    printf("Enter a sentence:\n");
    fgets(text, sizeof(text), stdin);

    for (int i = 0; text[i] != '\0'; i++) {

        if (text[i] != '\n')
            characters++;

        if (text[i] == ' ')
            words++, spaces++;

        if (isdigit(text[i]))
            digits++;

        if (isalpha(text[i])) {
            char ch = tolower(text[i]);

            if (ch=='a'||ch=='e'||ch=='i'||ch=='o'||ch=='u')
                vowels++;
            else
                consonants++;
        }

        if (!isalnum(text[i]) && text[i] != ' ' && text[i] != '\n')
            special++;
    }

    printf("\n===== TEXT ANALYSIS =====\n");
    printf("Characters        : %d\n", characters);
    printf("Words             : %d\n", words);
    printf("Vowels            : %d\n", vowels);
    printf("Consonants        : %d\n", consonants);
    printf("Digits            : %d\n", digits);
    printf("Spaces            : %d\n", spaces);
    printf("Special Characters: %d\n", special);

    return 0;
}