/**
<h1> 1.03: Differansen mellom to heltall </h1>
*/

import java.util.Scanner;

class Differanse {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        System.out.println("Oppgi verdien til x: ");
        int x = Integer.parseInt(in.next());

        System.out.println("Oppgi verdien til y: ");
        int y = Integer.parseInt(in.next());

        int sum = x+y;
        System.out.println("Differansen mellom x og y er " + sum);
    }
}
