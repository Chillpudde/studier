public class TestProgram {
    public static void main(String[] args) {
        Regneklynge r1 = new Regneklynge(2);
        Node n1 = new Node(64);
        r1.settInnRack();
        r1.settInnNode(n1);
    }
}
