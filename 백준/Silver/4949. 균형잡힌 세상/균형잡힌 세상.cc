#include <iostream>
#include <vector>
using namespace std;

int main() {
    char c[101];
    bool chk = false;
    while (!chk) {
        cin.getline(c, 101);
        int len = 0;
        bool chk2 = false;
        vector<char> v;
        for (int i = 0; i < 101; i++)
        {
            if (c[i] == '.') {
                if (!len) chk = true;
                else if (v.size()) cout << "no\n";
                else cout << "yes\n";
                break;
            }
            if (c[i] == '(') v.push_back('(');
            else if (c[i] == '[') v.push_back('[');
            else if (c[i] == ')') {
                if (!v.size() || v.back() != '(') { cout << "no\n"; break; }
                v.pop_back();
            }
            else if (c[i] == ']') {
                if (!v.size() || v.back() != '[') { cout << "no\n"; break; }
                v.pop_back();
            }
            len++;
        }
    }
    return 0;
}
