import java.util.ArrayList;
import java.util.Scanner;

public class StudentList {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        ArrayList<String> students = new ArrayList<>();

        int choice;

        do {
            System.out.println("\n===== STUDENT LIST =====");
            System.out.println("1. Add Student");
            System.out.println("2. View Students");
            System.out.println("3. Remove Student");
            System.out.println("4. Search Student");
            System.out.println("5. Exit");

            System.out.print("Enter Choice: ");
            choice = sc.nextInt();
            sc.nextLine();

            switch (choice) {

                case 1:
                    System.out.print("Enter Student Name: ");
                    String name = sc.nextLine();

                    students.add(name);
                    System.out.println("Student Added Successfully!");
                    break;

                case 2:
                    System.out.println("\n----- Student List -----");

                    if (students.isEmpty()) {
                        System.out.println("No students found.");
                    } else {
                        for (int i = 0; i < students.size(); i++) {
                            System.out.println((i + 1) + ". " + students.get(i));
                        }
                    }
                    break;

                case 3:
                    System.out.print("Enter Student Name to Remove: ");
                    String removeName = sc.nextLine();

                    if (students.remove(removeName)) {
                        System.out.println("Student Removed!");
                    } else {
                        System.out.println("Student Not Found!");
                    }
                    break;

                case 4:
                    System.out.print("Enter Student Name to Search: ");
                    String searchName = sc.nextLine();

                    if (students.contains(searchName)) {
                        System.out.println("Student Found!");
                    } else {
                        System.out.println("Student Not Found!");
                    }
                    break;

                case 5:
                    System.out.println("Program Ended.");
                    break;

                default:
                    System.out.println("Invalid Choice!");
            }

        } while (choice != 5);

        sc.close();
    }
}