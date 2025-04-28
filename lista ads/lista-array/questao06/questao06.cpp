#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

struct cordenada {
    double x, y;
};

double distancia(cordenada p1, cordenada p2) {
    return sqrt(pow(p1.x - p2.x, 2) + pow(p1.y - p2.y, 2));
}

double menor_distancia(cordenada pontos[], int n) {
    double menor = distancia(pontos[0], pontos[1]);
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            double d = distancia(pontos[i], pontos[j]);
            if (d < menor) menor = d;
        }
    }
    return menor;
}

int main() {
    int n;
    cin >> n;
    cordenada pontos[n];
    for (int i = 0; i < n; ++i) cin >> pontos[i].x >> pontos[i].y;
    cout << fixed << setprecision(4) << menor_distancia(pontos, n) << endl;
    return 0;
}
