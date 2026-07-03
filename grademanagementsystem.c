#include <stdio.h>

struct Student {
    int roll;
    char name[50];
    float marks1, marks2, marks3;
    float percentage;
    char grade;
};

int main() {
    struct Student s;

    printf("===== Student Grade Management System =====\n\n");

    printf("Enter Roll Number: ");
    scanf("%d", &s.roll);

    printf("Enter Name: ");
    scanf(" %[^\n]", s.name);

    printf("Enter Marks of Subject 1: ");
    scanf("%f", &s.marks1);

    printf("Enter Marks of Subject 2: ");
    scanf("%f", &s.marks2);

    printf("Enter Marks of Subject 3: ");
    scanf("%f", &s.marks3);

    s.percentage = (s.marks1 + s.marks2 + s.marks3) / 3;

    if(s.percentage >= 90)
        s.grade = 'A';
    else if(s.percentage >= 75)
        s.grade = 'B';
    else if(s.percentage >= 60)
        s.grade = 'C';
    else if(s.percentage >= 40)
        s.grade = 'D';
    else
        s.grade = 'F';

    printf("\n========== RESULT ==========\n");
    printf("Roll Number : %d\n", s.roll);
    printf("Name        : %s\n", s.name);
    printf("Percentage  : %.2f%%\n", s.percentage);
    printf("Grade       : %c\n", s.grade);

    return 0;
}