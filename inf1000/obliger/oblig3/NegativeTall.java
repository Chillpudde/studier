class NegativeTall {
    public static void main(String[] args) {
        int[] heltall = {1, 4, 5, -2, -4, 6, 10, 3, -2};
        int count = 0;

        //Teller antall tall
        while(count < heltall.length) {
            count++;
        }
        System.out.println(count + "\n");

        //Erstatter alle negative tall med sin posisjon
        int i = 0;
        while(i < heltall.length) {
            if (heltall[i] < 0) {
                heltall[i] = i;
            }
            System.out.print(heltall[i] + " ");
            i++;
        }
    }
}
