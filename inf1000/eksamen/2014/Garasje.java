import java.util.HashMap;

class Garasje {
    private Bil[] biler = new Bil[10];
    private int antBiler = 9;

    HashMap<LeieAvtale, Bil> leie = new HashMap<LeieAvtale, Bil>();
    static Person eier = new Person("Fredrik Olsen", "201283 53258");

    public Garasje() {
        biler[0] = new Bil("Volvo", "V60", 2010, 2010, 49000);
        biler[1] = new Bil("Volvo", "V60", 2010, 2010, 49000);
        biler[2] = new Bil("Volvo", "V60", 2010, 2010, 49000);
        biler[3] = new Bil("Skoda", "Octavia", 2009, 2012, 150000);
        biler[4] = new Bil("Skoda", "Octavia", 2009, 2012, 170000);
        biler[5] = new Bil("Skoda", "Octavia", 2009, 2012, 185000);
        biler[6] = new Bil("Fiat", "500", 2013, 2013, 205000);
        biler[7] = new Bil("Fiat", "500", 2013, 2013, 205000);
        biler[8] = new Bil("Fiat", "500", 2013, 2013, 205000);
    }

    public int sumInnkjopspris() {
        int sum = 0;
        for (int i = 0; i < biler.length; i++) {
            if (biler[i] != null) {
                sum += biler[i].getInnkjopspris();
            }
        }
        return sum;
    }

    public boolean kjopBil(String merke, String modell, int aarsmodell, int innkjopsaar, int pris) {
        if (antBiler < 10) {
            biler[antBiler] = new Bil(merke, modell, aarsmodell, innkjopsaar, pris);
            antBiler++;
            return true;
        }
        System.out.println("Det er ikke plass til flere biler i garasjen.");
        return false;
    }
}
