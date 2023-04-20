public class App {
    public static void main(String[] args) throws Exception {
        Table myTab = new Table(5, 5, ".");
        System.out.println(myTab);
        myTab.add("X", 0, 3);
        myTab.add("O", 3, 1);
        System.out.println(myTab);
        myTab.erase(3, 1);
        myTab.erase(0, 3);
        System.out.println(myTab);
        myTab.clear();
        System.out.println(myTab);

    }
}
