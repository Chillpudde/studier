/**
Oppgave 01.1: Person, Oppgave 01.2: Hus
*/

class PersonMain {
    public static void main(String[] args) {
        Person a = new Person("Bjarne");
        Person b = new Person("Kari");

        Hus hus1 = new Hus(a);
        System.out.println(hus1.getNavn());

        System.out.println(a.getNavn());
        System.out.println(b.getNavn());
    }
}
