/**
* <h1> Obligatorisk oppgave INF1000 2015, oppgave 1.1 </h1>
*/
import java.util.Scanner;

class HeiStudent {
    public static void main(String[] args) {
        System.out.println("Hei Student!"); // a)

        String navn = "navn"; // b)
        System.out.println("Hei " + navn);

        Scanner lesInn = new Scanner(System.in); // c)
        String navnInn = lesInn.next();
        System.out.println("Hei " + navnInn);

        int a = Integer.parseInt(lesInn.next()); // d) og e)
        int b = Integer.parseInt(lesInn.next());
        int res = a+b;
        System.out.println("Summen av a og b = " + res);
    }
}
