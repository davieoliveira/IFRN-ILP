#include <iostream>
#include <unordered_set>

using namespace std;

int contarDistintos(int A[], int n) {
    unordered_set<int> elementos;
    
    for (int i = 0; i < n; ++i) {
        elementos.insert(A[i]);
    }
    
    return elementos.size();
}

int main() {
    int n;
    cout << "Digite o tamanho do array (1 <= n <= 10^4): ";
    cin >> n;

    if (n < 1 || n > 1e4) {
        cout << "Tamanho invalido! Deve ser 1 <= n <= 10^4." << endl;
        return 1;
    }

    int A[n];
    cout << "Digite os " << n << " elementos do array (-10^6 <= Ai <= 10^6):" << endl;
    for (int i = 0; i < n; ++i) {
        cin >> A[i];
    }

    int distintos = contarDistintos(A, n);
    cout << "Quantidade de numeros distintos: " << distintos << endl;

    return 0;
}