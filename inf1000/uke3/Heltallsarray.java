class Heltallsarray {
    public static void main(String[] args) {
        int a = 0;
        int b = 1;
        int c = 2;
        int d = 3;
        int e = 4;

        System.out.println(a + " " + b + " " + c + " " + d + " " + e);

        int[] x = new int[5];
        int i = 0;
        while (i < x.length) {
            x[i] = i;
            i++;
        }

        int j = 0;
        while (i < x.length) {
            System.out.println(x[j]);
            j++;
        }
    }
}
