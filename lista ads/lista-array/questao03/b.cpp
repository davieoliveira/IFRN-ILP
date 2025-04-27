#include <iostream>

void conta_positivos_negativos(int a[], int n, int positivos[], int& qtd_positivos, int negativos[], int& qtd_negativos) {
    for (int i = 0; i < n; ++i) {
        if (a[i] > 0) {
            positivos[qtd_positivos] = a[i];
            qtd_positivos++;
        } else if (a[i] < 0) {
            negativos[qtd_negativos] = a[i];
            qtd_negativos++;
        }
    }
}

int main() {
    int n, qtd_positivos = 0, qtd_negativos = 0;
    std::cin >> n;
    int a[n], positivos[n], negativos[n];

    for (int i = 0; i < n; ++i) {
        std::cin >> a[i];
    }

    conta_positivos_negativos(a, n, positivos, qtd_positivos, negativos, qtd_negativos);

    std::cout << "Quantidade de positivos: " << qtd_positivos << std::endl;
    if (qtd_positivos > 0) {
        std::cout << "Positivos: " << positivos[0];
        for (int i = 1; i < qtd_positivos; ++i) {
            std::cout << " " << positivos[i];
        }
        std::cout << std::endl;
    }

    std::cout << "Quantidade de negativos: " << qtd_negativos << std::endl;
    if (qtd_negativos > 0) {
        std::cout << "Negativos: " << negativos[0];
        for (int i = 1; i < qtd_negativos; ++i) {
            std::cout << " " << negativos[i];
        }
        std::cout << std::endl;
    }

    return 0;
}