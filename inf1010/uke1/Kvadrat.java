import java.lang.Math.*;

public class Kvadrat {
    private double side;
    private double areal;
    private double omkrets;

    public Kvadrat(double side) {
        this.side = side;
    }

    public double beregnAreal() {
        areal = side*side;
        return areal;
    }

    public double beregnOmkrets() {
        omkrets = side*4;
        return omkrets;
    }
}
