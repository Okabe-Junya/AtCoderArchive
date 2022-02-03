#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int main(void){
    // Your code here!
    int n, k;
    long long h = 0;
    cin >> n >> k;
    vector<int> D(n);
    for(int i=0; i < n; i++){
        cin >> D.at(i);
    }
    if(n < k){
        cout << 0 << endl;
    }
    else{
        sort(D.begin(), D.end());
        for(int i=0; i < n-k; i++){
            h += D.at(i);
        }
        cout << h << endl;
    }
}
