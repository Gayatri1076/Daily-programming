import java.util.ArrayList;
import java.util.Scanner;

class Expense {
    String category;
    double amount;

    Expense(String category, double amount) {
        this.category = category;
        this.amount = amount;
    }
}

public class ExpenseTracker {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        ArrayList<Expense> expenses = new ArrayList<>();

        int choice;

        do {
            System.out.println("\n===== EXPENSE TRACKER =====");
            System.out.println("1. Add Expense");
            System.out.println("2. View Expenses");
            System.out.println("3. Show Total");
            System.out.println("4. Exit");
            System.out.print("Enter Choice: ");

            choice = sc.nextInt();
            sc.nextLine();

            switch (choice) {

                case 1:
                    System.out.print("Enter Category: ");
                    String category = sc.nextLine();

                    System.out.print("Enter Amount: ");
                    double amount = sc.nextDouble();

                    if (amount > 0) {
                        expenses.add(new Expense(category, amount));
                        System.out.println("Expense Added Successfully!");
                    } else {
                        System.out.println("Invalid Amount!");
                    }
                    break;

                case 2:
                    if (expenses.isEmpty()) {
                        System.out.println("No Expenses Available.");
                    } else {
                        System.out.println("\n----- Your Expenses -----");

                        for (int i = 0; i < expenses.size(); i++) {
                            Expense e = expenses.get(i);

                            System.out.println(
                                (i + 1) + ". " +
                                e.category + " - ₹" +
                                e.amount
                            );
                        }
                    }
                    break;

                case 3:
                    double total = 0;

                    for (Expense e : expenses) {
                        total += e.amount;
                    }

                    System.out.println("Total Expenses: ₹" + total);
                    break;

                case 4:
                    System.out.println("Thank You for using Expense Tracker!");
                    break;

                default:
                    System.out.println("Invalid Choice!");
            }

        } while (choice != 4);

        sc.close();
    }
}