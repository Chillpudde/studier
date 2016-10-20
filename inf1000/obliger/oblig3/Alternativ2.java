class Alternativ2 {
    public static void main(String[] args) {
        int[] poeng = {23, 32, 40, 0, 16, 26, 22, -10, 41};

        skrivKarakterprotokoll(poeng);
    }

    static void skrivKarakterprotokoll(int[] poeng) {
        for (int kandNr = 0; kandNr < poeng.length; kandNr++) {
            if (poeng[kandNr] < 0 || poeng[kandNr] > 40) {
                System.out.println("Kandidatnummer " + kandNr + " : UGYLDIG" + "\n");
            } else if (poeng[kandNr] >= 36 && poeng[kandNr] <= 40) {
                System.out.println("Kandidatnummer " + kandNr + " : A" + "\n");
            } else if (poeng[kandNr] >= 31 && poeng[kandNr] <= 35 ) {
                System.out.println("Kandidatnummer " + kandNr + " : B" + "\n");
            } else if (poeng[kandNr] >= 23 && poeng[kandNr] <= 34) {
                System.out.println("Kandidatnummer " + kandNr + " : C" + "\n");
            } else if (poeng[kandNr] >= 18 && poeng[kandNr] <= 22) {
                System.out.println("Kandidatnummer " + kandNr + " : D" + "\n");
            } else if (poeng[kandNr] >= 16 || poeng[kandNr] == 17) {
                System.out.println("Kandidatnummer " + kandNr + " : E" + "\n");
            } else {
                System.out.println("Kandidatnummer " + kandNr + " : F" + "\n");
            }
        }
    }
}
