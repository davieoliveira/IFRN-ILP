#include <iostream>

void maior_soma_consecutivos(int a[], int n, int& maior_soma) {
    if (n < 2) {
        maior_soma = 0; 
        return;
    }

    maior_soma = a[0] + a[1]; 
    
    for (int i = 1; i < n - 1; ++i) {
        int soma_atual = a[i] + a[i + 1];
        if (soma_atual > maior_soma) {
            maior_soma = soma_atual;
        }
    }
}

int main() {
    int n;
    std::cin >> n;
    
    if (n < 2) {
        std::cout << "O array deve ter pelo menos 2 elementos." << std::endl;
        return 0;
    }

    int a[n];
    for (int i = 0; i < n; ++i) {
        std::cin >> a[i];
    }

    int resultado;
    maior_soma_consecutivos(a, n, resultado);

    std::cout << "A maior soma de dois numeros consecutivos e: " << resultado << std::endl;

    return 0;
}