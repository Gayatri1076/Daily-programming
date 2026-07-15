#include <stdio.h>
#include <stdlib.h>

int main() {
    FILE *source, *destination;
    char sourceFile[100], destFile[100];
    char ch;

    printf("===== FILE COPY UTILITY =====\n");

    printf("Enter Source File Name: ");
    scanf("%s", sourceFile);

    printf("Enter Destination File Name: ");
    scanf("%s", destFile);

    source = fopen(sourceFile, "r");

    if (source == NULL) {
        printf("Error! Source file not found.\n");
        return 1;
    }

    destination = fopen(destFile, "w");

    while ((ch = fgetc(source)) != EOF) {
        fputc(ch, destination);
    }

    fclose(source);
    fclose(destination);

    printf("\nFile copied successfully!\n");

    return 0;
}