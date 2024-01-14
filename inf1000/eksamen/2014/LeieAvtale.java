class LeieAvtale {
    Person utleier = new Person("Fredrik Olsen", "201283 53258");
    Bil leiebil;
    Person leietaker;
    int maanedsleie;
    int[] fraDato = new int[3]; //0 = dag, 1 = mnd, 2 = aar

    public LeieAvtale(int dag, int mnd, int aar, int maanedsleie, Person leietaker, Bil leiebil) {
        fraDato[0] = dag;
        fraDato[1] = mnd;
        fraDato[2] = aar;
        this.maanedsleie = maanedsleie;
        this.leietaker = leietaker;
        this.leiebil = leiebil;

    }
}
