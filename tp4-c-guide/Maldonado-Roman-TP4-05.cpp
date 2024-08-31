#include<iostream>
using namespace std;

void promedio(){
	float nota1, nota2, nota3, promedio;

	cout << "> Porfavor digite su nota 1: " << endl;
	cin >> nota1;

	cout << "> Porfavor digite su nota 2: " << endl;
	cin >> nota2;

	cout << "> Porfavor digite su nota 3: " << endl; 
	cin >> nota3;

	promedio  = (nota1 + nota2 + nota3) / 3;
	cout << "> Su nota final es de: " << promedio << endl;
}

int main(){
	promedio();
	return 0;
}
