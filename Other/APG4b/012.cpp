#include <bits/stdc++.h>
using namespace std;

int main() {
  string S;
  cin >> S;
  int n = 1;
  for (int i = 1; i < S.size(); i+=2){
      char a = S.at(i);
      if (a == '+'){
          n += 1;
      }
      else{
          n -= 1;
      }
  }
  cout << n << endl;

  // ここにプログラムを追記
}

