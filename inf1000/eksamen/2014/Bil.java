class Bil {
    private String merke;
    private String modell;
    private int aarsmodell;
    private int innkjopsaar;
    private int innkjopspris;

    public Bil(String merke, String modell, int aarsmodell, int innkjopsaar, int innkjopspris) {
        this.merke = merke;
        this.modell = modell;
        this.aarsmodell = aarsmodell;
        this.innkjopsaar = innkjopsaar;
        this.innkjopspris = innkjopspris;
    }

    public int getInnkjopspris() {
        return innkjopspris;
    }

    public int getInnkjopsaar() {
        return innkjopsaar;
    }
}
