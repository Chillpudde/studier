/**
1.09: Skatt i Ruritania
*/

import java.util.Scanner;
class SkattRuritania {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        System.out.print("Inntekt: ");
        double inntekt = Double.parseDouble(in.next());
        double skatt = 0.0;

        if (inntekt < 10000) {
            skatt = inntekt*0.1;
        } else {
            skatt = (10000*0.1) + ((inntekt-10000)*0.3);
        }

        System.out.println("Skatt: " + skatt);
    }
}
