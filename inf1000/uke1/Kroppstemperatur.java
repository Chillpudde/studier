/**
1.10: Kroppstemperatur
*/

import java.util.Scanner;
class Kroppstemperatur {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        double minTemp = 36.5;
        double maksTemp = 37.5;

        System.out.print("Skriv inn din Kroppstemperatur: ");
        double innTemp = Double.parseDouble(in.next());

        if (innTemp < minTemp || innTemp > maksTemp) {
            System.out.println("Du har feber!");
        } else {
            System.out.println("Du er frisk!");
        }
    }
}
