#include <iostream>
#include <vector>
using namespace std;

int main(){
    int n, m;
    vector<int> a(m);
    vector<int> b(m);
    cin >> n >> m;
    for (int i = 0; i < m; i++){
        cin >> a[i] >> b[i];
    }
    for (int i = 0; i < n; i++)
    {
        int ans = 0;
        for (int j = 0; j < m; j++)
        {
            if (a[j]==i+1)
            {
                ans += 1;
            }
            if (b[j]==i+1)
            {
                ans += 1;
            }
            
        }
        
        cout << ans << endl;
        
    }
}