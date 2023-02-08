import java.util.Random;

public class App {
    public static void main(String[] args) throws Exception {
        Lamp lamp1 = new Lamp();
        System.out.println("Lamp1 is " + lamp1);
        Lamp[] lamp = new Lamp[30];
        Random rand = new Random();

        for (int i = 0; i < 30; i++) {
            boolean val = rand.nextBoolean();
            lamp[i] = new Lamp(val);
        }
        int count = 1;
        for (int i = 0; i < 30; i++) {
            System.out.print(lamp[i] + "   ");
            if (count % 5 == 0)
                System.out.println();
            count++;
        }

    }
}
