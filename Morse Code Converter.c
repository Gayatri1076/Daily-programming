#include <stdio.h>
#include <ctype.h>

int main() {

    char *morse[] = {
        ".-","-...","-.-.","-..",".","..-.","--.","....","..",".---",
        "-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-",
        "..-","...-",".--","-..-","-.--","--.."
    };

    char text[100];

    printf("===== MORSE CODE CONVERTER =====\n");
    printf("Enter Text: ");
    fgets(text, sizeof(text), stdin);

    printf("\nMorse Code:\n");

    for(int i = 0; text[i] != '\0'; i++) {

        if(text[i] >= 'A' && text[i] <= 'Z')
            printf("%s ", morse[text[i]-'A']);

        else if(text[i] >= 'a' && text[i] <= 'z')
            printf("%s ", morse[text[i]-'a']);

        else if(text[i] == ' ')
            printf("/ ");

    }

    return 0;
}