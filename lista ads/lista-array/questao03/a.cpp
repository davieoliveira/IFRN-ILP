#include <iostream>

void conta_pares(int a[], int n, int pares[], int& qtd_pares) {
    for (int i = 0; i < n; ++i) {
        if (a[i] % 2 == 0) {  // Verifica se o número é par
            pares[qtd_pares] = a[i];
            qtd_pares++;
        }
    }
}

int main() {
    int n, qtd_pares = 0;
    std::cin >> n;
    int a[n], pares[n];  // Array para armazenar os pares

    for (int i = 0; i < n; ++i) {
        std::cin >> a[i];
    }

    conta_pares(a, n, pares, qtd_pares);

    std::cout << "Quantidade de pares: " << qtd_pares << std::endl;

    if (qtd_pares > 0) {
        std::cout << "Pares: " << pares[0];
        for (int i = 1; i < qtd_pares; ++i) {
            std::cout << " " << pares[i];
        }
    }

    return 0;
}