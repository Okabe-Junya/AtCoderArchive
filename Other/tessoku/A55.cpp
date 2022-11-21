#include <iostream>
#include <set>

using namespace std;

int main(int argc, char const *argv[]) {
    int Q;
    cin >> Q;
    set<int> s;
    for (int i = 0; i < Q; i++) {
        int t, x;
        cin >> t >> x;
        if (t == 1) {
            s.insert(x);
        } else if (t == 2) {
            s.erase(x);
        } else {
            auto idx = s.lower_bound(x);
            if (idx == s.end()) {
                cout << -1 << endl;
            } else {
                cout << *idx << endl;
            }
        }
    }
    return 0;
}
