#include <iostream>
using namespace std;
int main(void){
    // Your code here!
    int n, k, m;
    int l = 0;
    cin >> n >> k >> m;
    int s = n * m;
    for(int i=0; i<n-1; i++){
        int a;
        cin >> a;
        l += a;
        
    }
    if(s < l){
        cout << 0 << endl;
    }
    else if (s > l + k){
        cout << -1 << endl;
        
    }
    else{
        cout << s - l<< endl;
    }
}