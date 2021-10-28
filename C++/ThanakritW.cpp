#include<bits/stdc++.h>
using namespace std;
string deleteduplicate(string x){
    string temp="";
    for(int i=0;i<x.length();i++){
        if(x[i]!=x[i+1]){
            temp+=x[i];
        }
    }
    return temp;
}
string changeFtoD(string x){
    string temp="";
    for(int i=0;i<x.length();i++){
        if(x[i]=='f')
            temp+='d';
        else 
            temp+=x[i];
    }
    return temp;
}
int main(){
    string c = "coffee";
    cout << changeFtoD(deleteduplicate(c));
    return 0;
}