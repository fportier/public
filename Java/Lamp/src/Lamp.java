public class Lamp {

    private boolean isOn;

    public Lamp() {
        this.isOn = false;
    }

    public Lamp(boolean isOn) {
        this.isOn = isOn;
    }

    public void turnOn() {
        this.isOn = true;
    }

    public void turnOff() {
        this.isOn = false;
    }

    public void flip() {
        this.isOn = !this.isOn;
    }

    public boolean isOn() {
        return this.isOn;
    }

    public void setLamp(boolean isOn) {
        this.isOn = isOn;
    }

    @Override
    public String toString() {
        String out;
        if (this.isOn)
            out = String.format("%3s", "ON");
        else
            out = String.format("%3s", "OFF");
        return out;
    }

    @Override
    public boolean equals(Object obj) {
        Lamp other = (Lamp) obj;
        if (isOn != other.isOn)
            return false;
        return true;
    }

}
