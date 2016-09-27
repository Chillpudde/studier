/**
Oppgave 01.1: Person, Oppgave 01.2: Hus
*/

class Person {
    private String navn;

    public Person (String navn) {
        this.navn = navn;
    }

    public String getNavn() {
        return navn;
    }
}

class Hus {
    private Person eier;

    public Hus(Person eier){
        this.eier = eier;
    }
}
