import java.util.Random;
import java.util.Scanner;

public class GuessNumberGame {
    public static void main(String[] args) {
        Random random = new Random();
        Scanner scanner = new Scanner(System.in);

        int secretNumber = random.nextInt(100) + 1;
        int guess;
        int attempts = 0;

        System.out.println("=== Number Guessing Game ===");
        System.out.println("I'm thinking of a number between 1 and 100.");

        do {
            System.out.print("Enter your guess: ");
            guess = scanner.nextInt();
            attempts++;

            if (guess < secretNumber) {
                System.out.println("Too low! Try again.");
            } else if (guess > secretNumber) {
                System.out.println("Too high! Try again.");
            } else {
                System.out.println("Congratulations!");
                System.out.println("You guessed the number in " + attempts + " attempts.");
            }

        } while (guess != secretNumber);

        scanner.close();
    }
}