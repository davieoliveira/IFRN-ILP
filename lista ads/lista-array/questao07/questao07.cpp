#include <iostream>
#include <unordered_set>

using namespace std;

bool existe_soma(int a[], int n, int s) {
    unordered_set<int> complementos;
    
    for (int i = 0; i < n; ++i) {
        int complemento = s - a[i];
        
        if (complementos.find(a[i]) != complementos.end()) {
            return true;
        }
        
        complementos.insert(complemento);
    }
    
    return false;
}

int main() {
    int n, s;
    cout << "Digite o tamanho do array: ";
    cin >> n;
    
    if (n < 2 || n > 10000) {
        cout << "Tamanho invalido!" << endl;
        return 1;
    }
    
    int a[n];
    cout << "Digite os " << n << " elementos do array:" << endl;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }
    
    cout << "Digite o valor da soma s (2*-10^9 <= s <= 2*10^9): ";
    cin >> s;
    
    if (existe_soma(a, n, s)) {
        cout << "Existem dois numeros no array cuja soma e " << s << "." << endl;
    } else {
        cout << "Nao existem dois numeros no array cuja soma e " << s << "." << endl;
    }
    
    return 0;
}