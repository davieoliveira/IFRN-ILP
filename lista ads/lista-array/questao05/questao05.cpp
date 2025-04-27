// 5. Escreva um algoritmo que receba um array A de n números inteiros e determine quantos elementos de A são primos.
// Incremente o programa para colocar os primos em outro array.
// Implemente e teste seu algoritmo em C++.
#include <iostream>
#include <cmath>

// Função para verificar se um número é primo
bool eh_primo(int num) {
    if (num <= 1) return false;
    if (num == 2) return true;
    if (num % 2 == 0) return false;
    
    for (int i = 3; i <= std::sqrt(num); i += 2) {
        if (num % i == 0) return false;
    }
    return true;
}

// Função que conta os primos e os coloca em outro array
void conta_primos(int a[], int n, int primos[], int& qtd_primos) {
    qtd_primos = 0;
    for (int i = 0; i < n; ++i) {
        if (eh_primo(a[i])) {
            primos[qtd_primos] = a[i];
            qtd_primos++;
        }
    }
}

int main() {
    int n, qtd_primos = 0;
    std::cout << "Digite o tamanho do array: ";
    std::cin >> n;
    
    int a[n], primos[n]; // O array de primos pode ter no máximo n elementos
    
    std::cout << "Digite os elementos do array:\n";
    for (int i = 0; i < n; ++i) {
        std::cin >> a[i];
    }
    
    conta_primos(a, n, primos, qtd_primos);
    
    std::cout << "Quantidade de numeros primos: " << qtd_primos << std::endl;
    
    if (qtd_primos > 0) {
        std::cout << "Numeros primos encontrados: ";
        std::cout << primos[0];
        for (int i = 1; i < qtd_primos; ++i) {
            std::cout << " " << primos[i];
        }
        std::cout << std::endl;
    } else {
        std::cout << "Nenhum numero primo encontrado." << std::endl;
    }
    
    return 0;
}