class Alternativ1 {
    public static void main(String[] args) {
        skrivTekster("Hei", 12);
    }

    static void skrivTekster(String tekst, int antall) {
        int count = 0;
        int linesplit = 0;

        while(count < antall) {
            if (linesplit > 2) {
                System.out.print("\n");
                linesplit = 0;
            }
            System.out.println(tekst);
            count++;
            linesplit++;
        }
    }
}
