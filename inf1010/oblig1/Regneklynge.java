import java.util.ArrayList;

class Regneklynge {
    int rackSize;
    public ArrayList<Rack> listeOverRacks = new ArrayList<Rack>();

    public Regneklynge(int rackSize) {
        this.rackSize = rackSize;
    }

    public void settInnNode(Node node) {
        for(int i = 0; i < listeOverRacks.size(); i++) {
            System.out.println("Node lagt til");
            listeOverRacks.get(i).leggTilNode(node);
            break;
        }
    }

    public void settInnRack() {
        Rack r = new Rack(rackSize);
        listeOverRacks.add(r);
    }
}
