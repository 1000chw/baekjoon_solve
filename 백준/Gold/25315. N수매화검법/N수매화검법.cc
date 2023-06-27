#include <iostream>
#include <algorithm>
#include <vector>
#define ll long long

using namespace std;

vector<vector<ll>> vec;

ll n;

bool ccw(ll n1, ll n2) {

    ll s1 = vec[n1][1] * vec[n1][4] + vec[n1][3] * vec[n2][2] + vec[n2][1] * vec[n1][2];
    s1 -= (vec[n1][3] * vec[n1][2] + vec[n2][1] * vec[n1][4] + vec[n1][1] * vec[n2][2]);

    ll s2 = vec[n1][1] * vec[n1][4] + vec[n1][3] * vec[n2][4] + vec[n1][2] * vec[n2][3];
    s2 -= (vec[n1][3] * vec[n1][2] + vec[n2][3] * vec[n1][4] + vec[n1][1] * vec[n2][4]);

    ll e1 = vec[n2][1] * vec[n2][4] + vec[n2][3] * vec[n1][2] + vec[n1][1] * vec[n2][2];
    e1 -= (vec[n2][3] * vec[n2][2] + vec[n1][1] * vec[n2][4] + vec[n1][2] * vec[n2][1]);

    ll e2 = vec[n2][1] * vec[n2][4] + vec[n2][3] * vec[n1][4] + vec[n1][3] * vec[n2][2];
    e2 -= (vec[n2][3] * vec[n2][2] + vec[n1][3] * vec[n2][4] + vec[n1][4] * vec[n2][1]);

    //cout << s1 <<  " " << s2 << " " << e1 << " " << e2;
    if (s1 > 0) s1 = 1;
    else if (s1 < 0) s1 = -1;
    else s1 = 0;
    if (s2 > 0) s2 = 1;
    else if (s2 < 0) s2 = -1;
    else s2 = 0;
    if (e1 > 0) e1 = 1;
    else if (e1 < 0) e1 = -1;
    else e1 = 0;
    if (e2 > 0) e2 = 1;
    else if (e2 < 0) e2 = -1;
    else e2 = 0;

    return (s1 * s2 <= 0 && e1 * e2 <= 0);

}

int main() {
    cin >> n;
    ll s_x, s_y, e_x, e_y;

    long long ans = 0;

    for (ll i = 0; i < n; i++) {
        ll w;
        vector<ll> vec2;

        cin >> s_x >> s_y >> e_x >> e_y >> w;
        vec2.push_back(w);
        vec2.push_back(s_x);
        vec2.push_back(s_y);
        vec2.push_back(e_x);
        vec2.push_back(e_y);
        vec.push_back(vec2);

    }

    sort(vec.begin(), vec.end());

    for (ll i = 0; i < n; i++) {
        ll m = 0;

        for (ll j = i + 1; j < n; j++) {
            if (ccw(i, j)) {
                m++;
            }
        }

        ans += (m + 1) * vec[i][0];
    }

    cout << ans;
    return 0;
}