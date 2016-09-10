/**
Obligatorisk oppgave 2, INF1000, 2016

av Andreas Johansen

Oppgave 2.3: While-lokker
*/

import java.util.Scanner;

class SumTall {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        System.out.println("Skriv inn tall. Tast 0 for aa avslutte:");
        boolean run = true;
        double sum = 0;

        while(run) {
            double tall = Double.parseDouble(in.next());
            sum += tall;

            if (tall == 0) {
                run = false;
            }
        }

        System.out.println("Summen er: " + sum);
    }
}
