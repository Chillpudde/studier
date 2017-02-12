class Kalkulator {
    public static void main(String[] args) {
        int svarAdd = addisjon(5, 4);
        int svarSub = subtraksjon(6, 10);
        int svarMult = mulitiplikasjon(23, 65);
        double svarDiv = divisjon(10, 3);

        System.out.println(svarAdd + " " + svarSub + " " + svarMult + " " + svarDiv);
    }

    public static int addisjon(int a, int b) {
        return a+b;
    }

    public static int subtraksjon(int a, int b) {
        return a-b;
    }

    public static int mulitiplikasjon(int a, int b) {
        return a*b;
    }

    public static double divisjon(double a, double b) {
        return a/b;
    }
}
