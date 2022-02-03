#include <iostream>
#include <string>
using namespace std;
int main(void){
    // Your code here!
    char a;
    string s;
    s = "abcdefghijklmnopqrstuvwxyz";
    cin >> a;
    for(int i=0; i < s.length(); i++){
        if (s[i] == a){
            cout << s[i+1] << endl;
        }
    }
}