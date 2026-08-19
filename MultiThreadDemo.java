class TaskOne extends Thread {

    public void run() {
        for (int i = 1; i <= 5; i++) {
            System.out.println("Task One: " + i);

            try {
                Thread.sleep(500);
            } catch (InterruptedException e) {
                System.out.println("Task One Interrupted");
            }
        }
    }
}

class TaskTwo extends Thread {

    public void run() {
        for (int i = 1; i <= 5; i++) {
            System.out.println("Task Two: " + i);

            try {
                Thread.sleep(500);
            } catch (InterruptedException e) {
                System.out.println("Task Two Interrupted");
            }
        }
    }
}

public class MultiThreadDemo {

    public static void main(String[] args) {

        TaskOne task1 = new TaskOne();
        TaskTwo task2 = new TaskTwo();

        task1.start();
        task2.start();
    }
}