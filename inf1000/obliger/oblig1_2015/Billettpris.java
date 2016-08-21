/**
* <h1> Obligatorisk oppgave INF1000 2015, oppgave 1.2 </h1>
*/

import java.util.Scanner;

class Billettpris {
    public static void main(String[] args) {
        Scanner lesInn = new Scanner(System.in);
        final int BILLETTPRIS = 50; // kr
        int alder = Integer.parseInt(lesInn.next());

        if (alder > 0 && alder < 12 || alder > 67) {
            System.out.println("Billettpris: " + BILLETTPRIS/2 + "kr");
        } else if ( alder < 0) {
            System.out.println("Ugyldig verdi.");
        } else {
            System.out.println("Billettpris: " + BILLETTPRIS + "kr");
        }
    }
}
