#include <iostream>
using namespace std;
int main(void){
    // Your code here!
    int h, a;
    cin >> h >> a;
    int ans;
    ans = h / a;
    if(a != 1 && h % a != 0){
        ans += 1;
    }
    cout << ans << endl;
}