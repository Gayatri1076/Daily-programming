import java.util.Scanner;

class Employee {
    int empId;
    String name;
    double basicSalary, hra, da, netSalary;

    void input(Scanner sc) {
        System.out.print("Enter Employee ID: ");
        empId = sc.nextInt();
        sc.nextLine();

        System.out.print("Enter Employee Name: ");
        name = sc.nextLine();

        System.out.print("Enter Basic Salary: ");
        basicSalary = sc.nextDouble();
    }

    void calculateSalary() {
        hra = basicSalary * 0.20;
        da = basicSalary * 0.10;
        netSalary = basicSalary + hra + da;
    }

    void display() {
        System.out.println("\n===== Employee Details =====");
        System.out.println("Employee ID : " + empId);
        System.out.println("Name        : " + name);
        System.out.println("Basic Salary: " + basicSalary);
        System.out.println("HRA         : " + hra);
        System.out.println("DA          : " + da);
        System.out.println("Net Salary  : " + netSalary);
    }
}

public class EmployeePayroll {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        Employee emp = new Employee();

        emp.input(sc);
        emp.calculateSalary();
        emp.display();

        sc.close();
    }
}