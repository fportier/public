public class Table implements Clearable {

    private String[][] tab;
    private int nrows;
    private int ncols;
    private int nmarks;
    private String clearSymbol;

    public Table(int nrows, int ncols, String clearSymbol) {
        this.ncols = ncols;
        this.nrows = nrows;
        this.nmarks = 0;
        this.clearSymbol = clearSymbol;
        this.tab = new String[this.nrows][];
        for (int i = 0; i < this.nrows; i++)
            this.tab[i] = new String[this.ncols];
        clear();
    }

    public String toString() {
        String out = "";
        for (int i = 0; i < this.nrows; i++) {
            for (int j = 0; j < this.ncols; j++)
                out += String.format("%3s", tab[i][j].toString());
            out += "\n";
        }
        return out;
    }

    public void clear() {
        for (int i = 0; i < this.nrows; i++)
            for (int j = 0; j < this.ncols; j++)
                this.tab[i][j] = this.clearSymbol;
        this.nmarks = 0;
    }

    public void add(String s, int x, int y) {
        this.tab[x][y] = s;
        this.nmarks++;
    }

    public void erase(int x, int y) {
        if (this.tab[x][y] != clearSymbol) {
            this.tab[x][y] = this.clearSymbol;
            this.nmarks--;
        }
    }

    public boolean inBounds(int x, int y) {
        return x > 0 && y > 0 && x < ncols && y < nrows;
    }

    public String[][] makeCopy() {
        String[][] copyTab = new String[this.nrows][];
        for (int i = 0; i < this.nrows; i++)
            copyTab[i] = new String[this.ncols];
        for (int i = 0; i < this.nrows; i++)
            for (int j = 0; j < this.ncols; j++)
                copyTab[i][j] = tab[i][j];
        return copyTab;
    }

    public boolean isEmpty() {
        return this.nmarks == 0;
    }

}
