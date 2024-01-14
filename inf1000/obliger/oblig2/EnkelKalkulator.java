/**
Obligatorisk oppgave 2, INF1000, 2016

av Andreas Johansen

Oppgave 2.1
*/

import java.util.Scanner;

class EnkelKalkulator {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        System.out.print("Skriv inn verdi for x: ");
        double x = Double.parseDouble(in.next());

        System.out.print("Skriv inn verdi for y: ");
        double y = Double.parseDouble(in.next());

        System.out.println("Summene og produktet av disse tallene blir: ");
        addere(x, y);
        subtrahere(x, y);
        multiplikasjon(x, y);
    }

    static void addere(double x, double y) {
        double sum = x + y;
        System.out.println(sum);
    }

    static void subtrahere(double x, double y) {
        double sum = x - y;
        System.out.println(sum);
    }

    static void multiplikasjon(double x, double y) {
        double produkt = x*y;
        System.out.println(produkt);
    }
}
