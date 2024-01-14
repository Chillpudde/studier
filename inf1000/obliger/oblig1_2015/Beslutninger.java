/**
* <h1> Obligatorisk oppgave INF1000 2015, oppgave 1.2 </h1>
*/

import java.util.Scanner;

class Beslutninger {
    public static void main(String[] args) {
        Scanner lesInn = new Scanner(System.in);
        int alder = Integer.parseInt(lesInn.next());
        if (alder >= 18) {
            System.out.println("Du er myndig");
        } else {
            System.out.println("Du er ikke myndig");
        }
    }
}
