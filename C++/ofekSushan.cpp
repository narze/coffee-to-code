#include <iostream>
#include <string>
using namespace std;

int main()
{
    bool replace = false;
    string coffee = "coffee";
    cout << coffee << endl;
    for (int index = 0; index < coffee.size() - 1; index++)
    {
        if (!replace && coffee[index] == 'f')
        {
            coffee[index] = 'd';

            replace = true;
        }
        else if (coffee[index] == 'f' || coffee[index] == 'e')
        {
            coffee.erase(index, 1);
            index--;
        }
    }

    cout << coffee << endl;

    return 0;
}
