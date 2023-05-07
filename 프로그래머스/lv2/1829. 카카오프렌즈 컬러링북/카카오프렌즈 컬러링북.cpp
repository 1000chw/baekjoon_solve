#include <vector>
#include <stack>
#include <iostream>
using namespace std;
int dx[4] = { 0, 1, 0, -1 };
int dy[4] = { 1, 0, -1, 0 };
vector<vector<bool>> visited;

// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
vector<int> solution(int m, int n, vector<vector<int>> picture) {
    int number_of_area = 0;
    int max_size_of_one_area = 0;
    visited = vector<vector<bool>>(m, vector<bool>(n, false));

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (picture[i][j] != 0 and !visited[i][j]) {
                number_of_area++;
                int size = 0;
                stack<int*> s;
                int* start = new int[3]{ i, j, picture[i][j] };
                s.push(start);
                while (!s.empty()) {
                    int* cur = s.top();
                    s.pop();
                    if (visited[cur[0]][cur[1]]) continue;
                    visited[cur[0]][cur[1]] = true;
                    size++;
                    for (int i = 0; i < 4; i++) {
                        int nx = dx[i] + cur[0];
                        int ny = dy[i] + cur[1];
                        if (0 <= nx and nx < m and 0 <= ny and ny < n and !visited[nx][ny] and picture[nx][ny] == cur[2]) {
                            int* next = new int[3]{ nx, ny, cur[2] };
                            s.push(next);
                        }
                    }
                }
                max_size_of_one_area = max(max_size_of_one_area, size);
            }
        }
    }

    vector<int> answer(2);
    answer[0] = number_of_area;
    answer[1] = max_size_of_one_area;
    return answer;
}
