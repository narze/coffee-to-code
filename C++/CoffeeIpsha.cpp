#include <iostream>
#include <string>
using namespace std;
int main() {
    string str = "Coffee";
    cout<<str<<"\n";
    str[2] = 'd';
    str[3] = 'e';
    str.resize(4);
    cout<<str;
    return 0;
}
