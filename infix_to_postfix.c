#include <stdio.h>
#include <ctype.h>

char stack[100];
int top = -1;

void push(char ch) {
    stack[++top] = ch;
}

char pop() {
    return stack[top--];
}

int precedence(char ch) {
    if(ch == '+' || ch == '-') return 1;
    if(ch == '*' || ch == '/') return 2;
    if(ch == '^') return 3;
    return 0;
}

int main() {
    char exp[100];

    printf("Enter Infix Expression: ");
    scanf("%s", exp);

    printf("Postfix Expression: ");

    for(int i = 0; exp[i] != '\0'; i++) {

        char ch = exp[i];

        if(isalnum(ch)) {
            printf("%c", ch);
        }
        else if(ch == '(') {
            push(ch);
        }
        else if(ch == ')') {
            while(top != -1 && stack[top] != '(')
                printf("%c", pop());
            pop();
        }
        else {
            while(top != -1 && precedence(stack[top]) >= precedence(ch))
                printf("%c", pop());

            push(ch);
        }
    }

    while(top != -1)
        printf("%c", pop());

    return 0;
}