import java.util.Scanner;

public class Q06 {
    public static void main(String[] args) {
        
        Scanner tec = new Scanner(System.in);

        int  maiorDiferenca = 0;

        int array_A[] = new int[5];

        for(int i = 0; i < array_A.length; i++) {
            System.out.print("Digite um número: ");

            array_A[i] = tec.nextInt();
        }

        tec.close();

        for(int i = 0; i < array_A.length - 1; i++) {

            if( array_A[i] - array_A[i  + 1] > maiorDiferenca) {
                maiorDiferenca = array_A[i] - array_A[i  + 1];
            }
        }

        System.out.println("O valor da maior diferença é: " + maiorDiferenca);

    }
}
