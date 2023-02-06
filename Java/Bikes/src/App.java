public class App {
    public static void main(String args[]) {
        MountainBike mb = new MountainBike(3, 100, 25);
        System.out.println(mb.toString());
        MountainBike b2 = new MountainBike(3, 100, 25);
        if (mb.equals(b2))
            System.out.println("equal");
        else
            System.out.println("not equal");
    }
}
