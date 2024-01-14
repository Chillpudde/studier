import java.util.Scanner;

class EnkelKalkulator2 {
    public static Scanner in = new Scanner(System.in);

    public static void main(String[] args) {

        System.out.println("Skriv inn to tall: " + "\n");
        System.out.print("Tall 1: ");
        double num1 = Double.parseDouble(in.next());

        System.out.print("\n" + "Tall 2: ");
        double num2 = Double.parseDouble(in.next());

        meny(num1, num2);
    }

    public static void addisjon(double num1, double num2) {
        System.out.println(num1+num2);
    }

    public static void subtraksjon(double num1, double num2) {
        System.out.println(num1-num2);
    }

    public static void multiplikasjon(double num1, double num2) {
        System.out.println(num1*num2);
    }

    public static void divisjon(double num1, double num2) {
        System.out.println(num1/num2);
    }

    public static void meny(double num1, double num2) {
        System.out.println("1. Addisjon"
        + "\n" + "2. Subtraksjon"
        + "\n" + "3. Multiplikasjon"
        + "\n" + "4. Divisjon");

        System.out.print("Valg: ");
        int valg = Integer.parseInt(in.next());
        switch(valg) {
            case 1: addisjon(num1, num2);
                break;
            case 2: subtraksjon(num1, num2);
                break;
            case 3: multiplikasjon(num1, num2);
                break;
            case 4: divisjon(num1, num2);
                break;
        }
    }
}
