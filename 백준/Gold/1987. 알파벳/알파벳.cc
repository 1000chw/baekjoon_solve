#include <iostream>
#include <cstring>
using namespace std;

int R, C, res = 0;
char arr[20][20];
bool visited[20][20], trace[27];
int dx[] = { 0, 0, -1, 1 };
int dy[] = { 1, -1, 0, 0 };

void solve(int x, int y, int n) {
    for (int i = 0; i < 4; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];
        if (0 <= nx && nx < R && 0 <= ny && ny < C && !trace[arr[nx][ny]-'A'] && !visited[nx][ny]) {
            trace[arr[nx][ny]-'A'] = true;
            visited[nx][ny] = true;
            solve(nx, ny, n + 1);
            visited[nx][ny] = false;
            trace[arr[nx][ny]-'A'] = false;
        }
    }
    res = max(res, n);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> R >> C;
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            cin >> arr[i][j];
        }
    }
    memset(visited, false, sizeof(visited));
    memset(trace, false, sizeof(trace));
    visited[0][0] = true;
    trace[arr[0][0]-'A'] = true;
    solve(0, 0, 1);
    cout << res << endl;
    return 0;
}
