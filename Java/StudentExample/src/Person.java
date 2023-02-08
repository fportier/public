public class Person {
    private String name = "NoName";
    private String citizen = "NoCitizenship";

    public Person(String name, String citizen) {
        this.name = name;
        this.citizen = citizen;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    @Override
    public boolean equals(Object obj) {
        Person other = (Person) obj;
        boolean c1 = this.name.equals(other.name);
        boolean c2 = this.citizen.equals(other.citizen);
        return c1 && c2;

    }

    public String getCitizen() {
        return citizen;
    }

    public void setCitizen(String citizen) {
        this.citizen = citizen;
    }

    @Override
    public String toString() {
        return "Person [name=" + name + ", citizen=" + citizen + "]";
    }

}
