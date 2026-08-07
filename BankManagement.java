import java.util.Scanner;

class BankAccount {
    int accountNumber;
    String accountHolder;
    double balance;

    void createAccount(Scanner sc) {
        System.out.print("Enter Account Number: ");
        accountNumber = sc.nextInt();
        sc.nextLine();

        System.out.print("Enter Account Holder Name: ");
        accountHolder = sc.nextLine();

        System.out.print("Enter Initial Balance: ");
        balance = sc.nextDouble();

        System.out.println("\nAccount Created Successfully!");
    }

    void deposit(Scanner sc) {
        System.out.print("Enter Deposit Amount: ");
        double amount = sc.nextDouble();

        if (amount > 0) {
            balance += amount;
            System.out.println("Deposit Successful!");
        } else {
            System.out.println("Invalid Amount!");
        }
    }

    void withdraw(Scanner sc) {
        System.out.print("Enter Withdrawal Amount: ");
        double amount = sc.nextDouble();

        if (amount > balance) {
            System.out.println("Insufficient Balance!");
        } else if (amount <= 0) {
            System.out.println("Invalid Amount!");
        } else {
            balance -= amount;
            System.out.println("Withdrawal Successful!");
        }
    }

    void checkBalance() {
        System.out.println("Current Balance: ₹" + balance);
    }
}

public class BankManagement {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        BankAccount account = new BankAccount();

        int choice;

        do {
            System.out.println("\n===== BANK MANAGEMENT SYSTEM =====");
            System.out.println("1. Create Account");
            System.out.println("2. Deposit");
            System.out.println("3. Withdraw");
            System.out.println("4. Check Balance");
            System.out.println("5. Exit");
            System.out.print("Enter Choice: ");

            choice = sc.nextInt();

            switch (choice) {
                case 1:
                    account.createAccount(sc);
                    break;

                case 2:
                    account.deposit(sc);
                    break;

                case 3:
                    account.withdraw(sc);
                    break;

                case 4:
                    account.checkBalance();
                    break;

                case 5:
                    System.out.println("Thank You!");
                    break;

                default:
                    System.out.println("Invalid Choice!");
            }

        } while (choice != 5);

        sc.close();
    }
}