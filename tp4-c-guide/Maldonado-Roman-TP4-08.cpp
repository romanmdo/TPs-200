#include <iostream>
using namespace std;

int mcd(int a, int b) {
    int resto;

    while (b != 0) {
        resto = a % b;
        a = b;
        b = resto;
    }

    return a;
}

int main(){
    int num1, num2;

    cout << "Ingresa A: ";
    cin >> num1;

    cout << "Ingresa B: ";
    cin >> num2;

    int resultado = mcd(num1, num2);
    cout << "El MCD es: " << resultado << endl;

    return 0;
}
