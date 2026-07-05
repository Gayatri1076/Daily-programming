#include <stdio.h>

int main() {
    int pin = 1234, enteredPin, choice, newPin;
    float balance = 10000.0, amount;

    printf("=================================\n");
    printf("      ATM MANAGEMENT SYSTEM\n");
    printf("=================================\n");

    printf("Enter Your 4-Digit PIN: ");
    scanf("%d", &enteredPin);

    if (enteredPin != pin) {
        printf("\nIncorrect PIN! Access Denied.\n");
        return 0;
    }

    do {
        printf("\n========== ATM MENU ==========\n");
        printf("1. Check Balance\n");
        printf("2. Deposit Money\n");
        printf("3. Withdraw Money\n");
        printf("4. Change PIN\n");
        printf("5. Exit\n");

        printf("Enter Your Choice: ");
        scanf("%d", &choice);

        switch (choice) {

            case 1:
                printf("\nCurrent Balance: ₹%.2f\n", balance);
                break;

            case 2:
                printf("Enter Deposit Amount: ₹");
                scanf("%f", &amount);

                if(amount <= 0)
                    printf("Invalid Amount!\n");
                else {
                    balance += amount;
                    printf("₹%.2f Deposited Successfully.\n", amount);
                }
                break;

            case 3:
                printf("Enter Withdrawal Amount: ₹");
                scanf("%f", &amount);

                if(amount > balance)
                    printf("Insufficient Balance!\n");
                else if(amount <= 0)
                    printf("Invalid Amount!\n");
                else {
                    balance -= amount;
                    printf("Please Collect Your Cash.\n");
                    printf("Remaining Balance: ₹%.2f\n", balance);
                }
                break;

            case 4:
                printf("Enter New 4-Digit PIN: ");
                scanf("%d", &newPin);

                pin = newPin;
                printf("PIN Changed Successfully!\n");
                break;

            case 5:
                printf("\nThank You for Using Our ATM.\n");
                break;

            default:
                printf("Invalid Choice!\n");
        }

    } while(choice != 5);

    return 0;
}