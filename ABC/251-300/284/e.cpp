#include <iostream>
#include <set>
#include <stack>
#include <tuple>
#include <vector>

using namespace std;

int main() {
    int N, M;
    cin >> N >> M;
    vector<vector<int> > tmpG(N);
    for (int _ = 0; _ < M; _++) {
        int u, v;
        cin >> u >> v;
        tmpG[u - 1].push_back(v - 1);
        tmpG[v - 1].push_back(u - 1);
    }
    int ans = 0;
    stack<pair<int, set<int> > > stack;
    set<int> tmpSet;
    tmpSet.insert(0);
    pair<int, set<int> > tmp;
    tmp.first = 0;
    tmp.second = tmpSet;
    stack.push(tmp);
    while (!stack.empty()) {
        pair<int, set<int> > tmp = stack.top();
        ans += 1;
        if (ans >= 1000000) {
            cout << "1000000" << endl;
            return 0;
        }
        for (int i : tmpG[tmp.first]) {
            if (tmp.second.count(i) == 0) {
                set<int> nextSet = tmp.second;
                nextSet.insert(i);
                pair<int, set<int> > next;
                next.first = i;
                next.second = nextSet;
                cout << "push " << i << endl;
                stack.push(next);
            }
        }
    }
    cout << ans << endl;
    return 0;
}
