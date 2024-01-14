/**
1.11: Ulike verdier
*/

import java.util.Scanner;
class UlikeVerdier {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        System.out.print("Velg verdi for i: ");
        int i = Integer.parseInt(in.next());
        System.out.print("Velg verdi for j: ");
        int j = Integer.parseInt(in.next());

        if (i == j) {
            System.out.println("i og j er like.");
        } else {
            System.out.println("i og j er IKKE like.");
        }
    }
}
