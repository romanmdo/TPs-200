#include <iostream>
#include <string>

using namespace std;

int main(){
    string text;

    cout << "> Hola, ingresa una cadena de texto!: " << endl;
    getline(cin, text);

    cout << "> La longitud de tu cadena de texto es de: " << text.length() << endl;
    return 0;
}