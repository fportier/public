import java.lang.Comparable;

public class ThreeNames
        implements Biggest, Comparable<ThreeNames> {

    private String[] list;
    private boolean[] occupied = { false, false, false };

    public ThreeNames() {
        this.list = new String[3];
        list[0] = list[1] = list[2] = "";
    }

    public ThreeNames(String s0, String s1, String s2) {
        this.list = new String[3];
        this.assign(0, s0);
        this.assign(1, s1);
        this.assign(2, s2);
    }

    public void assign(int pos, String name) {
        this.list[pos] = name;
        this.occupied[pos] = true;
    }

    public boolean validIndex(int pos) {
        return pos >= 0 && pos < 3;
    }

    public boolean notEmpty() {
        return !this.occupied[0] && !this.occupied[1] && !this.occupied[2];
    }

    public double max() {
        int len1 = this.list[0].length();
        int len2 = this.list[1].length();
        int len3 = this.list[2].length();
        return (double) Math.max(Math.max(len1, len2), len3);
    }

    @Override
    public String toString() {
        // String out = "---";
        String out = "";
        for (int i = 0; i < 3; i++) {
            out += i + ":";
            if (this.occupied[i])
                out += String.format("%-10s  ", this.list[i]) + "  ";
            else
                out += String.format("%-10s  ", "----------") + "  ";
        }
        return out;
    }

    private int check(int pos, ThreeNames obj) {
        return this.list[pos].compareTo(obj.list[pos]);
    }

    public int compareTo(ThreeNames obj) {
        int result = check(0, obj);
        if (result != 0)
            return result;
        else {
            result = check(1, obj);
            if (result != 0)
                return result;
            else
                return check(2, obj);
        }
    }

}
