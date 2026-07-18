#include <stdio.h>
#include <string.h>

int main() {
    char str1[100], str2[100];
    int freq1[26] = {0}, freq2[26] = {0};

    printf("Enter First String: ");
    scanf("%s", str1);

    printf("Enter Second String: ");
    scanf("%s", str2);

    if(strlen(str1) != strlen(str2)) {
        printf("Not Anagram");
        return 0;
    }

    for(int i = 0; str1[i] != '\0'; i++) {
        freq1[str1[i] - 'a']++;
        freq2[str2[i] - 'a']++;
    }

    for(int i = 0; i < 26; i++) {
        if(freq1[i] != freq2[i]) {
            printf("Not Anagram");
            return 0;
        }
    }

    printf("Anagram");

    return 0;
}