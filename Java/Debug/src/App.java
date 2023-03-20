public class App {
    public static void main(String[] args) {
        Seq test1 = new Seq(2, 3, 12);
        System.out.println(test1);
        Seq test2 = new Seq(3, 5, 10);
        System.out.println(test2);
        int val = inCommon(test1, test2);
        if (val != Integer.MIN_VALUE)
            System.out.println("First in common is " + val);
        else
            System.out.println("no match");
    }

    public static int inCommon(Seq seq1, Seq seq2) {
        int[] list1 = seq1.getSeq();
        int[] list2 = seq2.getSeq();
        for (int x : list1)
            if (inList(x, list2))
                return x;
        return Integer.MIN_VALUE;
    }

    public static boolean inList(int target, int[] lst) {
        for (int x : lst)
            if (x == target)
                return true;
        return false;
    }
}
