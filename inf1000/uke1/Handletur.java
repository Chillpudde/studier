/**
1.12: Handletur
*/

import java.util.Scanner;

class Handletur {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        final int BROD = 20; //kr
        final int MELK = 15;
        final int OST = 40;
        final int YOUGHURT = 12;

        System.out.print("Antall brod: ");
        int antBrod = Integer.parseInt(in.next());

        System.out.print("Antall melk: ");
        int antMelk = Integer.parseInt(in.next());

        System.out.print("Antall ost: ");
        int antOst = Integer.parseInt(in.next());

        System.out.print("Antall youghurt: ");
        int antYoughurt = Integer.parseInt(in.next());

        int sumBrod = BROD*antBrod;
        int sumMelk = MELK*antMelk;
        int sumOst = OST*antOst;
        int sumYoughurt = YOUGHURT*antYoughurt;

        int totalSum = sumBrod+sumMelk+sumOst+sumYoughurt;

        System.out.println("Handleturen kostet: " + totalSum + " kr.");
    }
}
