import java.math.BigInteger;

public class Main {

    public static void main(String[] args) {
        BigInteger A = new BigInteger("12630192673789351314");
        BigInteger B = new BigInteger("35234390061212433526");
        BigInteger M = new BigInteger("95034255219577607603");
        BigInteger X = new BigInteger("56687054115473550533");
        int count = 12;
        int k = 0;

        while (count != 0){
            System.out.println("X" + k + " is " + X);
            X = (A.multiply(X).add(B)).mod(M) ;


            count --;
            k++;
        }
    }
}
