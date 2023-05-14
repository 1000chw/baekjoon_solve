#include <vector>
#include <algorithm>
using namespace std;

bool comp(vector<int> x, vector<int> y) {
    if (x[1] < y[1]) return true;
    else return false;
}

// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
int solution(int n, vector<vector<int>> data) {
    int answer = 0;
    sort(data.begin(), data.end(), comp);

    bool chk = true;
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (data[i][0] != data[j][0] and data[i][1] != data[j][1]) {
                int Mx = max(data[i][0], data[j][0]);
                int mx = min(data[i][0], data[j][0]);
                for (int k = i + 1; k < j; k++) {
                    if (mx < data[k][0] and data[k][0] < Mx and data[i][1] < data[k][1] and data[k][1] < data[j][1]) {
                        chk = false;
                        break;
                    }
                }
                if (chk) answer++;
                chk = true;
            }
        }
    }
    return answer;
}