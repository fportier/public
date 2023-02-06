public class Bicycle {

    // this is the base class
    // the Bicycle class has two fields
    private int gear; // change from website
    private int speed; // chnange from website

    public Bicycle(int gear, int speed) {
        this.gear = gear;
        this.speed = speed;
    }

    public void applyBrake(int decrement) {
        speed -= decrement;
    }

    public void speedUp(int increment) {
        speed += increment;
    }

    @Override
    public String toString() {
        return ("No of gears are " + gear + "\n"
                + "speed of bicycle is " + speed);
    }

    @Override
    public boolean equals(Object obj) {
        Bicycle b2 = (Bicycle) obj;
        return this.gear == b2.gear && this.speed == b2.speed;
    }

}