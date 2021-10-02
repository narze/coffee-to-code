#include<iostream>
#include<string>

int main(){
	using namespace std;
	string coffee = "coffee", code;
	code = coffee;
	string changer = "d";
	code.replace(2, 3, changer);
	cout << code << "\n";
	return 0;
}
