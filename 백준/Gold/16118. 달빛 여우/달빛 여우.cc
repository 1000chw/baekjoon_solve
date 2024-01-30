#include <iostream>
#include <vector>
#include <queue>
#include <limits>
#include <tuple>
using namespace std;

const int INF = numeric_limits<int>::max();

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    vector<vector<pair<int, int>>> road(n + 1);
    for (int i = 0; i < m; ++i) {
        int a, b, d;
        cin >> a >> b >> d;
        road[a].push_back({d, b});
        road[b].push_back({d, a});
    }

    vector<int> dijk_fox(n + 1, INF);
    vector<vector<int>> dijk_wolf(2, vector<int>(n + 1, INF));
    dijk_fox[1] = 0;
    dijk_wolf[1][1] = 0;

    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq_fox;
    priority_queue<tuple<int, int, int, int>, vector<tuple<int, int, int, int>>, greater<tuple<int, int, int, int>>> pq_wolf;
    pq_fox.push(make_pair(0, 1));
    pq_wolf.push(make_tuple(0, 1, 4, 1));

    while (!pq_fox.empty()) {
        auto e = pq_fox.top();
        int d = e.first;
        int b = e.second;
        pq_fox.pop();
        if (dijk_fox[b] == d) {
            for (auto& r : road[b]) {
                int nb = r.second;
                int nd = d + r.first * 2;
                if (dijk_fox[nb] > nd) {
                    dijk_fox[nb] = nd;
                    pq_fox.push(make_pair(nd, nb));
                }
            }
        }
    }

    while (!pq_wolf.empty()) {
        auto w = pq_wolf.top();
        int d = get<0>(w);
        int b = get<1>(w);
        int v = get<2>(w);
        int ind = get<3>(w);
        pq_wolf.pop();
        if (v == 4) v = 1;
        else v = 4;
        if (dijk_wolf[ind][b] == d) {
            ind ^= 1;
            for (auto& x : road[b]) {
                int nd = x.first;
                int nb = x.second;
                nd = d + nd * v;
                if (dijk_wolf[ind][nb] > nd) {
                    dijk_wolf[ind][nb] = nd;
                    pq_wolf.push(make_tuple(nd, nb, v, ind));
                }
            }
        }
    }

    int res = 0;
    for (int i = 2; i <= n; ++i) {
        if (dijk_fox[i] < min(dijk_wolf[0][i], dijk_wolf[1][i])) {
            res++;
        }
    }
    cout << res << endl;

    return 0;
}
