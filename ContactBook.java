import java.util.HashMap;
import java.util.Scanner;

public class ContactBook {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        HashMap<String, String> contacts = new HashMap<>();

        int choice;

        do {
            System.out.println("\n===== CONTACT BOOK =====");
            System.out.println("1. Add Contact");
            System.out.println("2. View Contacts");
            System.out.println("3. Search Contact");
            System.out.println("4. Update Contact");
            System.out.println("5. Delete Contact");
            System.out.println("6. Exit");

            System.out.print("Enter Choice: ");
            choice = sc.nextInt();
            sc.nextLine();

            switch (choice) {

                case 1:
                    System.out.print("Enter Name: ");
                    String name = sc.nextLine();

                    System.out.print("Enter Phone Number: ");
                    String phone = sc.nextLine();

                    contacts.put(name, phone);
                    System.out.println("Contact Added Successfully!");
                    break;

                case 2:
                    System.out.println("\n----- All Contacts -----");

                    if (contacts.isEmpty()) {
                        System.out.println("No Contacts Found.");
                    } else {
                        for (String contact : contacts.keySet()) {
                            System.out.println(
                                contact + " : " + contacts.get(contact)
                            );
                        }
                    }
                    break;

                case 3:
                    System.out.print("Enter Name to Search: ");
                    String searchName = sc.nextLine();

                    if (contacts.containsKey(searchName)) {
                        System.out.println(
                            "Phone Number: " + contacts.get(searchName)
                        );
                    } else {
                        System.out.println("Contact Not Found!");
                    }
                    break;

                case 4:
                    System.out.print("Enter Name to Update: ");
                    String updateName = sc.nextLine();

                    if (contacts.containsKey(updateName)) {

                        System.out.print("Enter New Phone Number: ");
                        String newPhone = sc.nextLine();

                        contacts.put(updateName, newPhone);
                        System.out.println("Contact Updated Successfully!");

                    } else {
                        System.out.println("Contact Not Found!");
                    }
                    break;

                case 5:
                    System.out.print("Enter Name to Delete: ");
                    String deleteName = sc.nextLine();

                    if (contacts.remove(deleteName) != null) {
                        System.out.println("Contact Deleted Successfully!");
                    } else {
                        System.out.println("Contact Not Found!");
                    }
                    break;

                case 6:
                    System.out.println("Thank You!");
                    break;

                default:
                    System.out.println("Invalid Choice!");
            }

        } while (choice != 6);

        sc.close();
    }
}