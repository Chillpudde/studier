class Rack {
    int rackSize; // Hvor mange noder det er plass til.

    public Rack(int rackSize) {
        this.rackSize = rackSize;
    }

    Node[] nodeListe = new Node[rackSize];

    public void leggTilNode(Node n) {
        for (int i = 0; i < nodeListe.length; i++) {
            if (nodeListe[i] == null) {
                nodeListe[i] = n;
            } else {
                System.out.println("Rack er fullt.");
            }
        }
    }
}
