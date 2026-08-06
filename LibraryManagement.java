import java.util.Scanner;

class Book {
    int id;
    String title;
    String author;

    void addBook(Scanner sc) {
        System.out.print("Enter Book ID: ");
        id = sc.nextInt();
        sc.nextLine();

        System.out.print("Enter Book Title: ");
        title = sc.nextLine();

        System.out.print("Enter Author Name: ");
        author = sc.nextLine();
    }

    void displayBook() {
        System.out.println("\nBook ID    : " + id);
        System.out.println("Title      : " + title);
        System.out.println("Author     : " + author);
    }
}

public class LibraryManagement {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter Number of Books: ");
        int n = sc.nextInt();

        Book[] books = new Book[n];

        for (int i = 0; i < n; i++) {
            books[i] = new Book();
            System.out.println("\nEnter Details of Book " + (i + 1));
            books[i].addBook(sc);
        }

        System.out.println("\n========== BOOK LIST ==========");

        for (Book b : books) {
            b.displayBook();
        }

        System.out.print("\nEnter Book ID to Search: ");
        int searchId = sc.nextInt();

        boolean found = false;

        for (Book b : books) {
            if (b.id == searchId) {
                System.out.println("\nBook Found!");
                b.displayBook();
                found = true;
                break;
            }
        }

        if (!found) {
            System.out.println("Book Not Found!");
        }

        sc.close();
    }
}