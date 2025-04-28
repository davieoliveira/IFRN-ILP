#include <iostream>
#include <climits> 

using namespace std;

int somaMaximaSubarray(int A[], int n) {
    int soma_maxima = INT_MIN;
    int soma_atual = 0;

    for (int i = 0; i < n; ++i) {
        soma_atual += A[i];
        
        if (soma_atual > soma_maxima) {
            soma_maxima = soma_atual;
        }
        
        if (soma_atual < 0) {
            soma_atual = 0;
        }
    }
    
    return soma_maxima;
}

int main() {
    int n;
    cout << "Digite o tamanho do array: ";
    cin >> n;

    int* A = new int[n];
    cout << "Digite os " << n << " elementos do array:" << endl;
    for (int i = 0; i < n; ++i) {
        cin >> A[i];
    }

    int resultado = somaMaximaSubarray(A, n);
    cout << "A soma maxima de subarray contiguo e: " << resultado << endl;
    return 0;
}