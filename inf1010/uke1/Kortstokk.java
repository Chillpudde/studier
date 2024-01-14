import java.util.ArrayList;
import java.util.Arrays;
import java.util.Random;

public class Kortstokk {
    protected ArrayList<Kort> kortstokk = new ArrayList<Kort>();
    private Random trekker;
    private String[] farger = {"H", "K", "S", "R"};

    public void trekkKort() {
        int indeks = trekker.nextInt(kortstokk.size());
    }

    public boolean erTom() {
        return true;
    }

    public ArrayList<Kort> getKortstokk() {
        int j = 0;
        for (Kort i : kortstokk){
            System.out.println(kortstokk.toString());
            j++;
        }
        System.out.println(j);
        return kortstokk;
    }

    public void klargjorKortstokk() {
        int kortPerFarge = 13;
        for (int i = 0; i < farger.length; i++) {
            for (int j = 0; j < kortPerFarge; j++) {
                Kort etKort = new Kort(farger[i], j);
                kortstokk.add(etKort);
            }
        }

        int j = 0;
        for (Kort i : kortstokk){
            System.out.println(kortstokk.toString());
            j++;
        }
        System.out.println(j);
    }
}
