import java.util.Scanner;

class Honsegaard {
    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);

        System.out.println("En natt i honsegaarden" + "\n");

        System.out.print("Hvor mange honer bor paa garden?: ");
        int antHoner = Integer.parseInt(in.next());

        System.out.print("Sover bonden? (j/n): ");
        String valgBonde = in.next();

        System.out.print("\n" + "Kommer reven? (j/n): ");
        String valgRev = in.next();

        if (valgBonde.equalsIgnoreCase("n") && valgRev.equalsIgnoreCase("j")) {
            System.out.println("Bonde skyter reven, og selger skinnet for 190kr.");
        } else if (valgBonde.equalsIgnoreCase("j") && valgRev.equalsIgnoreCase("j")){
            antHoner--;
            System.out.println("Reven spiser en hone. Det er " + antHoner + " igjen paa gaarden.");

        } else {
            System.out.println("Natten gikk rolig for seg.");
        }
    }
}
