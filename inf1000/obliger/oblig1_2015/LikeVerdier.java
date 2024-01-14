/**
* <h1> Obligatorisk oppgave i INF1000 2015, oppgave 1.4 </h1>
*/

import java.util.Scanner;

class LikeVerdier {
    public static void main(String[] args) {
        Scanner lesInn = new Scanner(System.in);
        int c = Integer.parseInt(lesInn.next());
        int d = Integer.parseInt(lesInn.next());

        if (c == d) {
            System.out.println("c og d er like");
        } else {
            System.out.println("c og d er ikke like");
        }
    }
}
