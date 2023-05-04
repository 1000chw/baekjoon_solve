#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

int x_[] = { 0, 1, 0, -1 };
int y_[] = { 1, 0, -1, 0 };
int n;
vector<vector<char>> arr;

int dfs(int row, int col, vector<vector<char>>& arr) {
	int res = 0;
	arr[row][col] = 0;
	for (int i = 0; i < 4; i++) {
		int next_r = row + x_[i], next_c = col + y_[i];
		if (0 <= next_c && next_c < n && 0 <= next_r && next_r < n && arr[next_r][next_c] == '1') {
			res += dfs(next_r, next_c, arr);
		}
	}
	return res + 1;
}

int main()
{
	cin >> n;
	arr = vector<vector<char>>(n);
	for (int i = 0; i < n; i++) {
		string x;
		cin >> x;
		for(auto j:x){
			arr[i].push_back(j);
		}
	}

	vector<int> res;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (arr[i][j] == '1') {
				res.push_back(dfs(i, j, arr));
			}
		}
	}
	sort(res.begin(), res.end());
	cout << res.size() << '\n';
	for (auto i : res) {
		cout << i << '\n';
	}
	return 0;
}

