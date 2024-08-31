#include <iostream>
#include <string>
using namespace std;

int suma(){
    int a, b, result;

    cout << "> Ingresa el valor A:" << endl;
    cin >> a;
    cout << "> Ingresa el valor B:" << endl;
    cin >> b;

    result = a + b;
    cout << "> El resultado es: " << result << endl;
}

int resta(){
    int a, b, result;

    cout << "> Ingresa el valor A:" << endl;
    cin >> a;
    cout << "> Ingresa el valor B:" << endl;
    cin >> b;

    result = a - b;
    cout << "> El resultado es: " << result << endl;
}

int multiplicar(){
    int a, b, result;

    cout << "> Ingresa el valor A:" << endl;
    cin >> a;
    cout << "> Ingresa el valor B:" << endl;
    cin >> b;

    result = a * b;
    cout << "> El resultado es: " << result << endl;
}

int dividir(){
    int a, b, result;

    cout << "> Ingresa el valor A:" << endl;
    cin >> a;
    cout << "> Ingresa el valor B:" << endl;
    cin >> b;

    result = a % b;
    cout << "> El resultado es: " << result << endl;
}

int main(){
    int op;
    
    cout << "> Ingresa la opcion que deseas llevar a cabo: \n[1] - Suma\n[2] - Resta\n[3] - Multiplicacion\n[4] - Division\n[5] - Salir" << endl;
    cin >> op;

    if(op == 1){
        suma();
    }
    else if (op == 2){
        resta();
    }   
    else if (op == 3){
        multiplicar();
    }
    else if (op == 4){
        dividir();
    }
}

