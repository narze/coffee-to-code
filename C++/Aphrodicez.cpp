#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base :: sync_with_stdio(false);
    cin.tie(nullptr);

    string coffee = "coffee";
    map <string, string> convert = {{"co", "co"}, {"ff", "d"}, {"ee", "e"}};
    string code = "";
    for(int i = 0; i < (int)coffee.size(); i += 2) {
        code += convert[coffee.substr(i, 2)];
    }
    cout << code << "\n";
    return 0;
}