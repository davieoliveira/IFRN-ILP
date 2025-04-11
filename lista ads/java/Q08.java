import java.util.Scanner;

public class Q08 {

    public static void main(String[] args) {

        int contadorPares = 0;
        
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
                    contadorPares += 1;
                }
            }
        }

        System.out.print("Quantidade de pares encontrados: " + contadorPares);
    }
    
}

