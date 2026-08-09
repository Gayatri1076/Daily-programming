import java.time.LocalTime;

public class DigitalClock {
    public static void main(String[] args) {

        while (true) {

            LocalTime time = LocalTime.now();

            System.out.printf(
                "\rCurrent Time: %02d:%02d:%02d",
                time.getHour(),
                time.getMinute(),
                time.getSecond()
            );

            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                System.out.println("\nClock stopped.");
                break;
            }
        }
    }
}