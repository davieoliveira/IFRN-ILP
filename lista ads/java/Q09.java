import java.util.Scanner;

public class Q09 {
    public static void main(String[] args) {

        boolean emOrdem = true;

        Scanner tec = new Scanner(System.in);

        int[] array_A = new int[3];

        for(int i = 0; i <= array_A.length - 1 ; i++) {
            System.out.print("Digite um número: ");

            array_A[i] = tec.nextInt();
        }
        
        tec.close();

        for(int i = 0; i < array_A.length - 1 ; i++) {
            if(array_A[i] > array_A[i + 1]) {
                emOrdem = false;
            }
        }

        if(emOrdem) {
            System.out.println("Os números ESTÃO em ordem crescente.");
        }
        else {
            System.err.println("Os números NÃO ESTÃO em ordem crescente.");
        }

    }
}
