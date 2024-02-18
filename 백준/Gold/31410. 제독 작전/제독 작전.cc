#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#define INF 0x7fffffff
#define LLINF 0x7f7f7f7f7f7f
#define fastio ios::sync_with_stdio(0), cin.tie(NULL), cout.tie(NULL);
using namespace std;
using ll = long long;
using pi = pair<int, int>;
using pll = pair<ll, ll>;

int main() {
    fastio;

    ll n;
    cin >> n;

    vector<pll> v(n + 1);
    for (int i = 1; i <= n; i++) {
        cin >> v[i].first >> v[i].second;
    }
    sort(v.begin() + 1, v.end());

    ll cnt1 = v[1].second, cnt2 = v[n].second;
    for (ll i = 2; i <= n; i++) {
        cnt1 += (v[i].first - v[i - 1].first) * (i - 1);
        cnt1 += v[i].second;

        cnt2 += (v[n + 2 - i].first - v[n + 1 - i].first) * (i - 1);
        cnt2 += v[n + 1 - i].second;
    }

    ll a = v[n].second + (n - 1) * (v[n].first - v[n - 1].first);
    ll b = v[1].second + (n - 1) * (v[2].first - v[1].first);
    ll res = min(cnt1 - a, cnt2 - b);
    ll tmp = 0;
    
    for (ll i = 1; i < n; i++) {
        tmp = cnt1 - v[i].second - v[n].first + v[i].first;
        res = min(res, tmp);
        tmp = cnt2 - v[n + 1 - i].second - v[n + 1 - i].first + v[1].first;
        res = min(res, tmp);
    }


    cout << res;

    return 0;
}