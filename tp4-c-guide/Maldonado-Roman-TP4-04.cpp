#include <iostream>
using namespace std;

int main(){
    int num;
    int i;
    int aux;

    cout << "> Hola, ingresa un num" << endl;
    cin >> num;

    for(i = 1; i <= 10; i++){
        aux = i * num;
        cout << aux << endl;
    }
    
    return 0;
}