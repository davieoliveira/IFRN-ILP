#include <iostream>
#include <vector>

using namespace std;

bool estaOrdenado(const int A[], int n) {
    for (int i = 0; i < n - 1; ++i) {
        if (A[i] > A[i + 1]) {
            return false;
        }
    }
    return true;
}

int main() {
    int n;
    cout << "Digite o tamanho do array (2 <= n <= 10^8): ";
    cin >> n;

    if (n < 2 || n > 1e8) {
        cout << "Tamanho invalido! Deve ser 2 <= n <= 10^8." << endl;
        return 1;
    }

    int* A = new int[n];  // Alocação dinâmica para grandes arrays
    cout << "Digite os " << n << " elementos do array (-10^9 <= Ai <= 10^9):" << endl;
    for (int i = 0; i < n; ++i) {
        cin >> A[i];
    }

    if (estaOrdenado(A, n)) {
        cout << "O array esta ordenado de forma nao decrescente." << endl;
    } else {
        cout << "O array NAO esta ordenado de forma nao decrescente." << endl;
    }

    delete[] A;  // Libera a memória alocada
    return 0;
}