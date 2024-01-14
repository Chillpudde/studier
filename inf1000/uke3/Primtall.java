// Printer ut alle primtall lavere enn N.

import java.util.Scanner;

class Primtall {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        System.out.print("Skriv ut alle primtall lavere enn: ");
        int tallInn = Integer.parseInt(in.next());

        // Primtall er delelig med seg selv og 1.

        for (int i = tallInn; i != 0; i--) {
            for (int j = 1; j < i; j++) {
                System.out.println(i+"%"+j + " = "+ i%j);
            }
        }
    }
}
/*
import java.util.Scanner;

class Primtall {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int tall = Integer.parseInt(sc.nextLine());
        int teller = tall;

        while(teller > 1) {
            printPrimtall(teller);
            teller--;
        }
    }

    public static void printPrimtall(int tall) {
        int teller = tall-1;
        boolean funnet = false;

        System.out.println(funnet);
        while(teller > 1) {
            if(tall % teller == 0) {
                System.out.println(tall + "%" + teller + "=" + tall%teller);
                funnet = true;
            }
            teller--;
        }

        if(!funnet) {
            System.out.println("Fant primtall " + tall);
        }
    }
}
*/
