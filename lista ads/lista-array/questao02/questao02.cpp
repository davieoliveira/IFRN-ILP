#include <iostream>

int contador_impar(int a[], unsigned int n) {
    int contador_impar = 0;
    
    for (unsigned int i = 0; i < n; ++i) {
        if (a[i] % 2 != 0) {
            contador_impar++;
        }
    }
    return contador_impar;
}

int main() {
    unsigned int n;
    std::cin >> n; 
    int* a = new int[n]; 

    for (unsigned int i = 0; i < n; ++i) {
        std::cin >> a[i];
    }

    int quantidade_impares = contador_impar(a, n);
    std::cout << quantidade_impares << std::endl;
    return 0;
}
