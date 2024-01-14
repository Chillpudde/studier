/**
1.13: Hoyde
*/

import java.util.Scanner;

class Hoyde {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        double lavHoyde = 140;
        double hoyHoyde = 190;

        System.out.print("Skriv inn din hoyde (cm): ");
        double minHoyde = Double.parseDouble(in.next());

        if (minHoyde < lavHoyde) {
            System.out.println("Du er lav.");
        } else if (minHoyde > hoyHoyde) {
            System.out.println("Du er hoy.");
        } else {
            System.out.println("Du er gjennomsnittelig.");
        }
    }
}
