#include <iostream>
#include <cstdlib>
#include <ctime>

#include <Windows.h>

int main(){
    srand(time(0));

    std::cout << "Really slow, but fun, way to convert\n";

    std::string coffee = "coffee";
    std::string code = "";
    char letter;
    int cont = 0;
    int i = 0;

    std::cout << "Write coffee to convert: ";
    std::cin >> coffee;

    if(coffee == "coffee"){
        while(true){
            letter = (rand() % 26) + 97;
            if(letter == "code"[i]){
                code += letter;
                i++;
                if(code == "code"){
                    std::cout << "We did it! it took " << cont
                    << " attemps to convert, there is your string: " << code;
                    break;
                }
            }
            cont++;
        }
    }

    return 0;
}
