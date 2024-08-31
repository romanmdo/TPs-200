#include <iostream>
using namespace std;

int main(){
    int numero;

    cout << "> Hola, ingresa un numero" << endl;
    cin >> numero;

    if (numero % 2 == 0){
        cout << "> El numero " << numero << " es Par!" << endl;
    }

    else{
        cout << "> El numero " << numero << " es Impar!" << endl;
    }

    return 0;
}