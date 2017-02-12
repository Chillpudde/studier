import java.lang.Math.*;

public class Sirkel {
    private double radius;
    private double areal;
    private double omkrets;

    public Sirkel(double radius) {
        this.radius = radius;
    }

    public double beregnAreal() {
        areal = Math.PI*Math.pow(radius, 2);
        return areal;
    }

    public double beregnOmkrets() {
        omkrets = 2*Math.PI*radius;
        return omkrets;
    }
}
