import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

class Innlesing {
    public static void main(String[] args) throws FileNotFoundException {
        Scanner lesInn = new Scanner(new File("winnie.txt"));
        Scanner ord = new Scanner(System.in);

        String[] text = new String[242];

        // Leser inn
        for (int i = 0; i < text.length; i++) {
            text[i] = lesInn.next();
            System.out.println(text[i]);
        }

        int wordCounter = 0;

        System.out.print("\n" + "Sjekke antall forekomster av: ");
        String innlestOrd = ord.next();

        for (int i = 0; i < text.length; i++) {
            if (text[i].equalsIgnoreCase(innlestOrd)) {
                wordCounter++;
            }
        }

        System.out.println("\n"+"Antall forekomster av \'" + innlestOrd + "\': " + wordCounter);
    }
}
