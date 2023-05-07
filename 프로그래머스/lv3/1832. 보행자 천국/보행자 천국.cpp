#include <vector>
using namespace std;

int MOD = 20170805;
int dx[2] = { 0, 1 };
int dy[2] = { 1, 0 };
vector<vector<int>> dp0;
vector<vector<int>> dp1;
vector<vector<int>> visited1;
vector<vector<int>> visited2;
// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
int solve(int m, int n, int x, int y, int dir, vector<vector<int>>& city_map) {
    if (x == m-1 and y == n-1) return 1;
    if (city_map[x][y] == 1) return 0;
    if (visited1[x][y] and dir == 0) {
        return dp0[x][y];
    }
    if (visited2[x][y] and dir == 1) {
        return dp1[x][y];
    }
    switch (city_map[x][y])
    {
    case 0: {
        for (int i = 0; i < 2; i++)
        {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (nx < m && ny < n) {
                if (i == 0) {
                    int res = solve(m, n, nx, ny, 0, city_map) % MOD;
                    dp0[x][y] += res;
                    dp1[x][y] += res;
                }
                else {
                    int res = solve(m, n, nx, ny, 1, city_map) % MOD;
                    dp0[x][y] += res;
                    dp1[x][y] += res;
                }
            }
        }
        dp0[x][y] %= MOD;
        dp1[x][y] %= MOD;
        visited1[x][y] = 1;
        visited2[x][y] = 1;
        return dp0[x][y];
        break;
    }
    case 2: {
        int nx = x + dx[dir];
        int ny = y + dy[dir];
        if (nx < m && ny < n) {
            if (dir == 0) {
                dp0[x][y] = solve(m, n, nx, ny, dir, city_map) % MOD;
                visited1[x][y] = 1;
                return dp0[x][y];
            }
            else {
                dp1[x][y] = solve(m, n, nx, ny, dir, city_map) % MOD;
                visited2[x][y] = 1;
                return dp1[x][y];
            }
        }
        return 0;
        break;
    }
    default:
        break;
    }
}

int solution(int m, int n, vector<vector<int>> city_map) {
    int answer = 0;
    dp0 = vector<vector<int>>(m, vector <int>(n, 0));
    dp1 = vector<vector<int>>(m, vector <int>(n, 0));
    visited1 = vector<vector<int>>(m, vector <int>(n, 0));
    visited2 = vector<vector<int>>(m, vector <int>(n, 0));
    answer = solve(m, n, 0, 0, 0, city_map);
    return answer;
}
