public class Q10 {
    public static void main(String[] args) {
        
        int array_A[] = {10, 5, -17, 20, 50, -1, 3, -30, 10};
        int somaMax = 0;

        for(int i = 0; i < array_A.length; i++) {
            int somaAtual = 0;
            for(int j = i; j < array_A.length; j++) {
                somaAtual += array_A[j];

                if(somaAtual > somaMax) {
                    somaMax = somaAtual;
                }
            }
        }

        System.out.println(somaMax);

    }
}
