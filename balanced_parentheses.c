#include <stdio.h>
#include <string.h>

int main() {
    char exp[100], stack[100];
    int top = -1;
    int valid = 1;

    printf("Enter Expression: ");
    scanf("%s", exp);

    for (int i = 0; exp[i] != '\0'; i++) {

        if (exp[i] == '(' || exp[i] == '{' || exp[i] == '[') {
            stack[++top] = exp[i];
        }

        else if (exp[i] == ')' || exp[i] == '}' || exp[i] == ']') {

            if (top == -1) {
                valid = 0;
                break;
            }

            char ch = stack[top--];

            if ((exp[i] == ')' && ch != '(') ||
                (exp[i] == '}' && ch != '{') ||
                (exp[i] == ']' && ch != '[')) {
                valid = 0;
                break;
            }
        }
    }

    if (top != -1)
        valid = 0;

    if (valid)
        printf("\nBalanced Expression\n");
    else
        printf("\nNot Balanced\n");

    return 0;
}