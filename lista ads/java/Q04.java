import java.util.Scanner;

public class Q04 {
    public static void main(String[] args) {

        int contadorDivisores = 0;

        Scanner tec = new Scanner(System.in);

        System.out.print("Digite um número inteiro: ");
        int num = tec.nextInt();

        tec.close();

        for(int i = 1; i <= num; i++) {
            if (num % i == 0) {
                contadorDivisores += 1;
            }

        }

        if (contadorDivisores == 2) {
            System.out.print(num + " é primo!");
        }
        else {
            System.out.print(num + " não é primo!");
        }

    }
}