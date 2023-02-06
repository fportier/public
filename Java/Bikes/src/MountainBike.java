class MountainBike extends Bicycle {

    // the MountainBike subclass adds one more field
    private int seatHeight;

    // the MountainBike subclass has one constructor
    public MountainBike(int gear, int speed, int seatHeight) {
        super(gear, speed); // invoking base-class(Bicycle) constructor
        this.seatHeight = seatHeight;
    }

    public void setHeight(int seatHeight) {
        this.seatHeight = seatHeight;
    }

    @Override
    public String toString() {
        return (super.toString() + "\nseat height is "
                + seatHeight);
    }

    @Override
    public boolean equals(Object obj) {

        if (obj instanceof MountainBike) {
            MountainBike mb2 = (MountainBike) obj;
            return super.equals(mb2) && mb2.seatHeight == this.seatHeight;
        } else
            return false;
    }
}
