/**
Obligatorisk oppgave 2, INF1000, 2016

av Andreas Johansen

Oppgave 2.4: First Array
*/

import java.util.Scanner;

class FirstArray {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int[] a = new int[4];

        int i = 0;
        while (i < 4) {
            a[i] = i;
            System.out.println(a[i]);
            i++;

            if (i > 3) {
                System.out.println("\n");
            }
        }

        a[0] = 1337;
        a[3] = 1337;

        i = 0;
        while(i < 4) {
            System.out.println(a[i]);
            i++;
            if (i > 3) {
                System.out.println("\n");
            }
        }

        String[] text = new String[5];

        int j = 0;
        while (j < 5) {
            String textInn = in.next();
            text[j] = textInn;
            j++;

            if (j > 4) {
                System.out.println("\n");
            }
        }

        for (int k = 0; k < 5; k++) {
            System.out.println(text[k]);
        }
    }
}
