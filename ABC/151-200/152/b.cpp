#include <iostream>
using namespace std;
int main(void){
    // Your code here!
    int a, b;
    cin >> a >> b;
    if (a > b){
        swap(a,b);
    }
    for(int i=0; i < b; i++){
        cout << a;
    }
    cout << endl;
}