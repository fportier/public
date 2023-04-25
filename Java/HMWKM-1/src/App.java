import java.util.ArrayList;
import java.util.List;
import java.util.Collections;

public class App {
    public static void main(String[] args) throws Exception {
        List<ThreeNames> list = getData();
        print(list);
        System.out.println("\nXXXXXXXXXXXXXXXXXXXXXXX\n");
        Collections.sort(list);
        print(list);
    }

    public static List<ThreeNames> getData() {
        List<ThreeNames> list = new ArrayList<ThreeNames>();
        list.add(new ThreeNames("b", "a", "x"));
        list.add(new ThreeNames("A", "B", "C"));
        list.add(new ThreeNames("XX", "D", "E"));
        list.add(new ThreeNames("A", "B", "A"));
        list.add(new ThreeNames("XX", "E", "F"));
        list.add(new ThreeNames("XX", "E", "E"));
        list.add(new ThreeNames("A", "B", "C"));
        list.add(new ThreeNames("a", "b", "c"));
        list.add(new ThreeNames("   ", "b", ""));

        ThreeNames e1 = new ThreeNames();
        e1.assign(0, "XX");
        e1.assign(2, "13");
        list.add(e1);

        ThreeNames e2 = new ThreeNames();
        e2.assign(1, "XX");
        e2.assign(2, "13");
        list.add(e2);

        ThreeNames e3 = new ThreeNames();
        list.add(e3);

        return list;
    }

    public static void print(List<ThreeNames> list) {
        for (ThreeNames x : list)
            System.out.println(x);
    }
}
