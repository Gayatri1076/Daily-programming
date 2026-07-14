#include <stdio.h>

int main() {
    FILE *fp;
    char ch;

    fp = fopen("students.csv", "r");

    if (fp == NULL) {
        printf("Error: Unable to open file!\n");
        return 1;
    }

    printf("===== STUDENT CSV DATA =====\n\n");

    while ((ch = fgetc(fp)) != EOF) {
        printf("%c", ch);
    }

    fclose(fp);

    return 0;
}