#include <bits/stdc++.h>
using namespace std;

int main() {
  vector<int> data(5);
  for (int i = 0; i < 5; i++) {
    cin >> data.at(i);
  }
  int a = 0;
  for (int i = 1; i < 5; i++){
    if(data[i]==data[i-1]){
      cout << "YES" << endl;
      break;
    }
    else{
      a += 1;
    }
  }
  if (a == 4){
    cout << "NO" << endl;
  }


  // dataの中で隣り合う等しい要素が存在するなら"YES"を出力し、そうでなければ"NO"を出力する
  // ここにプログラムを追記
}