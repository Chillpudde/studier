/**
<h1> 1.06: Regn ut produktet av to heltall
*/

import java.util.Scanner;
class Produkt {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        System.out.println("Skriv inn to tall som skal multipliseres:");
        int x = Integer.parseInt(in.next());
        int y = Integer.parseInt(in.next());

        int res = x*y;
        System.out.println("Prduktet av tallene er: " + res);
    }
}
