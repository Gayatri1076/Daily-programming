import java.util.ArrayList;
import java.util.Scanner;

class Bus {
    int busNo;
    String source;
    String destination;
    int totalSeats;
    int bookedSeats;

    Bus(int busNo, String source, String destination, int totalSeats) {
        this.busNo = busNo;
        this.source = source;
        this.destination = destination;
        this.totalSeats = totalSeats;
        this.bookedSeats = 0;
    }

    void display() {
        System.out.println("----------------------------");
        System.out.println("Bus Number : " + busNo);
        System.out.println("Source     : " + source);
        System.out.println("Destination: " + destination);
        System.out.println("Total Seats: " + totalSeats);
        System.out.println("Booked     : " + bookedSeats);
        System.out.println("Available  : " + (totalSeats - bookedSeats));
    }

    void bookSeat() {
        if (bookedSeats < totalSeats) {
            bookedSeats++;
            System.out.println("Seat booked successfully!");
        } else {
            System.out.println("Sorry! No seats available.");
        }
    }
}

public class BusManagementSystem {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        ArrayList<Bus> buses = new ArrayList<>();

        while (true) {

            System.out.println("\n===== BUS MANAGEMENT SYSTEM =====");
            System.out.println("1. Add Bus");
            System.out.println("2. View All Buses");
            System.out.println("3. Search Bus");
            System.out.println("4. Book Seat");
            System.out.println("5. Exit");
            System.out.print("Enter Choice: ");

            int choice = sc.nextInt();

            switch (choice) {

                case 1:
                    System.out.print("Enter Bus Number: ");
                    int no = sc.nextInt();

                    sc.nextLine();

                    System.out.print("Enter Source: ");
                    String source = sc.nextLine();

                    System.out.print("Enter Destination: ");
                    String destination = sc.nextLine();

                    System.out.print("Enter Total Seats: ");
                    int seats = sc.nextInt();

                    buses.add(new Bus(no, source, destination, seats));

                    System.out.println("Bus Added Successfully!");
                    break;

                case 2:
                    if (buses.isEmpty()) {
                        System.out.println("No buses available.");
                    } else {
                        for (Bus b : buses) {
                            b.display();
                        }
                    }
                    break;

                case 3:
                    System.out.print("Enter Bus Number to Search: ");
                    int search = sc.nextInt();

                    boolean found = false;

                    for (Bus b : buses) {
                        if (b.busNo == search) {
                            b.display();
                            found = true;
                            break;
                        }
                    }

                    if (!found) {
                        System.out.println("Bus Not Found.");
                    }
                    break;

                case 4:
                    System.out.print("Enter Bus Number: ");
                    int book = sc.nextInt();

                    boolean booked = false;

                    for (Bus b : buses) {
                        if (b.busNo == book) {
                            b.bookSeat();
                            booked = true;
                            break;
                        }
                    }

                    if (!booked) {
                        System.out.println("Bus Not Found.");
                    }
                    break;

                case 5:
                    System.out.println("Thank You!");
                    sc.close();
                    System.exit(0);

                default:
                    System.out.println("Invalid Choice!");
            }
        }
    }
}