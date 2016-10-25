import java.util.Scanner;
import java.io.FileReader;
import java.util.ArrayList;
import java.io.FileNotFoundException;

class Temperatur {
    public static void main(String[] args) throws FileNotFoundException {
        printArrayList(lesInn());
        gjenTemp(lesInn());
    }

    static ArrayList<Integer> lesInn() throws FileNotFoundException {
        Scanner dataInn = new Scanner(new FileReader("temperatur.txt"));

        ArrayList<Integer> dataList = new ArrayList<Integer>();

        while (dataInn.hasNext()) {
            int data = Integer.parseInt(dataInn.next());
            dataList.add(data);
        }

        return dataList;
    }

    static void printArrayList(ArrayList<Integer> liste) {
        for (Integer i : liste) {
            System.out.println(i);
        }
    }

    static void gjenTemp(ArrayList<Integer> liste) {
        int sum = 0;
        int antElementer = 0;

        for (Integer i : liste) {
            sum += i;
            antElementer++;
        }
        
        double gjenSnitt = sum/antElementer;
        System.out.println("\n" + gjenSnitt);
    }
}
