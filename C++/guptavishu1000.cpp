#include<bits/stdc++.h>
using namespace std;
int main(){
	ios_base::sync_with_stdio(0); cin.tie(NULL); cout.tie(NULL);
	string s="coffee";
	unordered_set<char>unique_characters(s.rbegin(),s.rend());
	string ans;
	for(char c:unique_characters){
		if((c-'a')%2)ans+=(char)((int)c-2);
		else ans+=c;
	}
	cout<<ans;
	return 0;
} 

