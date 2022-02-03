#include <iostream>
using namespace std;
int main(void){
    // Your code here!
    int h, n;
    cin >> h >> n;
    int ans = 0;
    for(int i=0; i<n; i++){
        int a;
        cin >> a;
        ans += a;
    }
    if (ans >= h){
        cout << "Yes" << endl;
    }
    else{
        cout << "No" << endl;
    }
}

