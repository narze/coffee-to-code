#include <iostream>
using namespace std;

int main(){
	char key = 's';
	string message = "Coffee to code";
	string output;
	
    cout << "Ascii code:";
	for(int i = 0; i < sizeof(message); i++){
		if(message[i]!=0)
		{
			printf("%c",message[i] ^ key);
		}
		output[i] = message[i] ^ key;
	}

	cout << "\n" << "Decrypt message: ";
	
	for(int i = 0; i < sizeof(output); i++){
		printf("%c",output[i] ^ key);
	}
	
	return 0;
}