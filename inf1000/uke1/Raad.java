/**
Oppgave 1.15: Har du raad?
*/

import java.util.Scanner;

class Raad {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        System.out.print("Skriv inn saldo: ");
        double saldo = Double.parseDouble(in.next());

        System.out.print("Hva koster varen?: ");
        double varepris = Double.parseDouble(in.next());

        if (varepris > saldo) {
            System.out.println("Du har ikke raad.");
        } else {
            System.out.println("Du har raad.");
        }
    }
}
