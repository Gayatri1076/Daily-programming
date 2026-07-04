#include <stdio.h>
#include <stdlib.h>

struct Account {
    int accNo;
    char name[50];
    float balance;
};

void createAccount() {
    FILE *fp = fopen("bank.dat", "ab");
    struct Account a;

    printf("\nEnter Account Number: ");
    scanf("%d", &a.accNo);

    printf("Enter Account Holder Name: ");
    scanf(" %[^\n]", a.name);

    printf("Enter Initial Balance: ");
    scanf("%f", &a.balance);

    fwrite(&a, sizeof(a), 1, fp);
    fclose(fp);

    printf("\nAccount Created Successfully!\n");
}

void displayAccounts() {
    FILE *fp = fopen("bank.dat", "rb");
    struct Account a;

    printf("\n===== ACCOUNT DETAILS =====\n");

    while (fread(&a, sizeof(a), 1, fp)) {
        printf("\nAccount No : %d", a.accNo);
        printf("\nName       : %s", a.name);
        printf("\nBalance    : %.2f\n", a.balance);
    }

    fclose(fp);
}

void depositMoney() {
    FILE *fp = fopen("bank.dat", "rb+");
    struct Account a;
    int acc;
    float amount;

    printf("Enter Account Number: ");
    scanf("%d", &acc);

    while (fread(&a, sizeof(a), 1, fp)) {
        if (a.accNo == acc) {
            printf("Enter Deposit Amount: ");
            scanf("%f", &amount);

            a.balance += amount;

            fseek(fp, -sizeof(a), SEEK_CUR);
            fwrite(&a, sizeof(a), 1, fp);

            printf("Deposit Successful!\n");
            fclose(fp);
            return;
        }
    }

    printf("Account Not Found!\n");
    fclose(fp);
}

void withdrawMoney() {
    FILE *fp = fopen("bank.dat", "rb+");
    struct Account a;
    int acc;
    float amount;

    printf("Enter Account Number: ");
    scanf("%d", &acc);

    while (fread(&a, sizeof(a), 1, fp)) {
        if (a.accNo == acc) {

            printf("Enter Withdraw Amount: ");
            scanf("%f", &amount);

            if (amount > a.balance) {
                printf("Insufficient Balance!\n");
            } else {
                a.balance -= amount;

                fseek(fp, -sizeof(a), SEEK_CUR);
                fwrite(&a, sizeof(a), 1, fp);

                printf("Withdrawal Successful!\n");
            }

            fclose(fp);
            return;
        }
    }

    printf("Account Not Found!\n");
    fclose(fp);
}

int main() {

    int choice;

    do {
        printf("\n====== BANK MANAGEMENT SYSTEM ======\n");
        printf("1. Create Account\n");
        printf("2. Display Accounts\n");
        printf("3. Deposit Money\n");
        printf("4. Withdraw Money\n");
        printf("5. Exit\n");

        printf("Enter Choice: ");
        scanf("%d", &choice);

        switch(choice) {
            case 1:
                createAccount();
                break;
            case 2:
                displayAccounts();
                break;
            case 3:
                depositMoney();
                break;
            case 4:
                withdrawMoney();
                break;
            case 5:
                printf("Thank You!\n");
                break;
            default:
                printf("Invalid Choice!\n");
        }

    } while(choice != 5);

    return 0;
}