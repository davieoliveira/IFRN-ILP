import java.util.Scanner;

public class Q07 {

    public static void main(String[] args) {

        boolean existePar = false;
        
        Scanner tec = new Scanner(System.in);

        int array_A[] = new int[6];

        for(int i = 0; i < array_A.length; i++){
            System.out.print("Digite um número: ");

            array_A[i] = tec.nextInt();
        }

        System.out.print("Digite um número alvo: ");
        int numAlvo = tec.nextInt();

        tec.close();

        for(int i = 0; i < array_A.length; i++) {
            for(int j = i + 1; j < array_A.length; j++) {

                if(array_A[i] + array_A[j] == numAlvo) {
                    existePar = true;
                }
            }
        }

        System.out.print(existePar);
    }
    
}
