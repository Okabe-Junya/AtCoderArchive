#include <iostream>
using namespace std;
int main(void){
    // Your code here!
    int n;
    cin >> n;
    int m;
    m = 1000000;
    int ans = 0;
    int a;
    for(int i=0; i < n; i++){
        cin >> a;
        if (a < m){
            m = a;
            ans += 1;
        }
        
        
    }
    cout << ans << endl;
    
}