import java.util.Scanner;

class Student {
    int rollNo;
    String name;
    double marks;

    void input(Scanner sc) {
        System.out.print("Enter Roll Number: ");
        rollNo = sc.nextInt();
        sc.nextLine(); // Consume newline

        System.out.print("Enter Name: ");
        name = sc.nextLine();

        System.out.print("Enter Marks: ");
        marks = sc.nextDouble();
    }

    void display() {
        System.out.println("\n----- Student Details -----");
        System.out.println("Roll Number : " + rollNo);
        System.out.println("Name        : " + name);
        System.out.println("Marks       : " + marks);
    }
}

public class StudentManagement {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter Number of Students: ");
        int n = sc.nextInt();

        Student[] students = new Student[n];

        for (int i = 0; i < n; i++) {
            students[i] = new Student();
            System.out.println("\nEnter Details of Student " + (i + 1));
            students[i].input(sc);
        }

        System.out.println("\n========== STUDENT RECORDS ==========");

        for (Student student : students) {
            student.display();
        }

        sc.close();
    }
}s