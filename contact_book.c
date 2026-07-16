#include <stdio.h>
#include <string.h>

struct Contact {
    char name[50];
    char phone[15];
};

int main() {
    struct Contact contacts[100];
    int n = 0, choice, i;
    char search[50];

    do {
        printf("\n===== CONTACT BOOK =====\n");
        printf("1. Add Contact\n");
        printf("2. Display Contacts\n");
        printf("3. Search Contact\n");
        printf("4. Exit\n");
        printf("Enter Choice: ");
        scanf("%d", &choice);

        switch(choice) {

            case 1:
                printf("Enter Name: ");
                scanf(" %[^\n]", contacts[n].name);

                printf("Enter Phone Number: ");
                scanf("%s", contacts[n].phone);

                n++;
                printf("Contact Added Successfully!\n");
                break;

            case 2:
                printf("\n----- CONTACT LIST -----\n");

                if(n == 0) {
                    printf("No Contacts Found!\n");
                } else {
                    for(i = 0; i < n; i++) {
                        printf("\nName : %s\n", contacts[i].name);
                        printf("Phone: %s\n", contacts[i].phone);
                    }
                }
                break;

            case 3:
                printf("Enter Name to Search: ");
                scanf(" %[^\n]", search);

                int found = 0;

                for(i = 0; i < n; i++) {
                    if(strcmp(search, contacts[i].name) == 0) {
                        printf("\nContact Found\n");
                        printf("Name : %s\n", contacts[i].name);
                        printf("Phone: %s\n", contacts[i].phone);
                        found = 1;
                        break;
                    }
                }

                if(!found)
                    printf("Contact Not Found!\n");

                break;

            case 4:
                printf("Thank You!\n");
                break;

            default:
                printf("Invalid Choice!\n");
        }

    } while(choice != 4);

    return 0;
}