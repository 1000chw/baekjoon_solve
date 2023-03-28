 #include <iostream>
using namespace std;

int main() {

   ios_base::sync_with_stdio(false);
   cin.tie(NULL);

   int x1, x2, y1, y2, p1, p2, q1, q2;

   for(int i=0;i<4;i++){
      cin >> x1 >> y1 >> p1 >> q1 >> x2 >> y2 >> p2 >> q2;
      if (x1 > p2 || p1 < x2 || y1 > q2 || q1 < y2) cout << "d\n";
      else if (y1 == q2 || y2 == q1){
        if (x1 == p2 || p1 == x2) cout << "c\n";
        else cout << "b\n";
      }
      else if (x1 == p2 || p1 == x2){
        if (y1 == q2 || y2 == q1) cout << "c\n";
        else cout << "b\n";
      }
      else cout << "a\n";
   }
}