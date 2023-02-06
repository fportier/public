public class App {
    //
    //
    //
    public static void main(String args[]) {
        MountainBike b = new MountainBike(10, 20, 4);
        MountainBike b2 = new MountainBike(10, 20, 4);
        b.speedUp(0);
        b.setHeight(6);
        System.out.println(b);
        b2.setHeight(6);
        System.out.println(b2);
        if (b.equals(b2))
            System.out.println("equal");
        else
            System.out.println("not equal");
    }
}
