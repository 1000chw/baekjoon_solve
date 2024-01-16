#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    int csod = 0;

    for (int i = 2; i <= n / 2; ++i) {
        csod += ((n / i - 1) * i) % 1000000;
        csod %= 1000000;
    }

    cout << csod % 1000000 << '\n';

    return 0;
}