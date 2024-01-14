/**
1.14: Busstur
*/

import java.util.Scanner;

class Busstur {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int plasser = 30;
        int passasjerer = 0;
        int i = 0;

        for (i = i; i < 3; i++) {
            if (plasser > 0) {
                System.out.print("Stasjon " + (i+1) + "! Hvor mange gaar paa bussen?: ");
                plasser = plasser - (Integer.parseInt(in.next()));

                if (plasser < 0) {
                    System.out.println("Bussen er full! " + (plasser - passasjerer)*(-1) + " maa gaa.");
                }
            }
        }
    }
}
