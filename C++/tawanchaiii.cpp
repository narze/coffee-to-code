#include<bits/stdc++.h>
using namespace std;
int main(){
  string str = "I would like to drink Coffee. Coffee!!";
  int pos = 0;
  while (1){
    pos = str.find("Coffee", pos);
    if (pos == std::string::npos)
      break;
    str.replace(pos,6,"Code");  
  }
  cout << str;
  return 0;
}