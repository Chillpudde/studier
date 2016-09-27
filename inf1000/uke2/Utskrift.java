class Utskrift {
    public static void main(String[] args) {
        utskrift("TEST");
        utskrift(1, 2);
    }

    public static void utskrift(String text) {
        System.out.println(text);
    }

    public static void utskrift(int num1, int num2) { // Metoder kan ha samme navn, men ufint!
        System.out.println(num1 + num2);
    }
}
