import java.util.Scanner;

class Stringarray {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] text = new String[5];

        int i = 0;
        while (i < text.length) {
            text[i] = sc.next();
            i++;
        }

        int j = 0;
        while (j < text.length) {
            System.out.println(text[j] + " ");
            j++;
        }
    }
}
