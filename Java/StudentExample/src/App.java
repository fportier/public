public class App {
    public static void main(String[] args) throws Exception {
        Person p1 = new Person("Joe", "US");
        System.out.println(p1);

        Student s = new Student("Tina", "France", "Upper Pine University");
        System.out.println(s);
        Student s2 = new Student("Harry", "France", "Upper Pine University");

        if (s.equals(s2))
            System.out.println("equal");
        else
            System.out.println("not equal");
    }
}
