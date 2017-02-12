/**
Oppgave 1.1 Person og 1.2 Hus
*/

public class TestProgram {
    public static void main(String[] args) {
        Person ole = new Person("Ole");
        Person bjarne = new Person("Bjarne");
        Hus h1 = new Hus(ole);

        //h1.printEier();
    }
}


/**
Sette eller ikke sette peker i konstruktør?
Man kan sette peker i konstruktøren om objektet allerede har blitt opprettet.
Om objektet ikke eksistere på det tidspunktet må den settes senere.

Man må spørre seg om det er noen hensikt i at det ene objektet eksisterer uten
det andre. Et hus kan fint eksistere uten eier, men i denne konteksten gir det
ikke mening.
*/
