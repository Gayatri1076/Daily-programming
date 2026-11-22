import java.util.HashMap;
import java.util.Scanner;

public class ConsoleRegistration {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        HashMap<String, String> users = new HashMap<>();

        System.out.println("=== User Registration ===");
        
        System.out.print("Enter Username: ");
        String username = scanner.nextLine();

        // Check if username already exists
        if (users.containsKey(username)) {
            System.out.println("Error: Username already exists!");
        } else {
            System.out.print("Enter Password: ");
            String password = scanner.nextLine();
            
            users.put(username, password);
            System.out.println("Registration successful for " + username + "!");
        }

        scanner.close();
    }
}