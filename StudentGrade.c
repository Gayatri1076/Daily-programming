#include <stdio.h>

struct Student {
    char name[50];
    int roll;
    float marks[5];
    float total, percentage;
    char grade;
};

int main() {
    int n;

    printf("Enter number of students: ");
    scanf("%d", &n);

    struct Student s[n];

    for(int i = 0; i < n; i++) {
        printf("\nStudent %d\n", i + 1);

        printf("Enter Roll No: ");
        scanf("%d", &s[i].roll);

        printf("Enter Name: ");
        scanf(" %[^\n]", s[i].name);

        s[i].total = 0;

        printf("Enter marks of 5 subjects:\n");
        for(int j = 0; j < 5; j++) {
            scanf("%f", &s[i].marks[j]);
            s[i].total += s[i].marks[j];
        }

        s[i].percentage = s[i].total / 5;

        if(s[i].percentage >= 90)
            s[i].grade = 'A';
        else if(s[i].percentage >= 75)
            s[i].grade = 'B';
        else if(s[i].percentage >= 60)
            s[i].grade = 'C';
        else if(s[i].percentage >= 40)
            s[i].grade = 'D';
        else
            s[i].grade = 'F';
    }

    printf("\n========== RESULT ==========\n");

    for(int i = 0; i < n; i++) {
        printf("\nRoll No    : %d", s[i].roll);
        printf("\nName       : %s", s[i].name);
        printf("\nTotal      : %.2f", s[i].total);
        printf("\nPercentage : %.2f%%", s[i].percentage);
        printf("\nGrade      : %c\n", s[i].grade);
    }

    return 0;
}