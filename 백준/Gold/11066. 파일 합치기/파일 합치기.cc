#include <iostream>
#include <algorithm>
using namespace std;

int m[501];
int dp[501][501];
int sum[501] = { 0, };

int solve(int left, int right)
{
	if (left == right)
		return 0;
	int& res = dp[left][right];
	if (res != -1)
		return res;
	if (left + 1 == right)
		return dp[left][right] = m[left] + m[right];
	res = 100000000;
	for (int i = left; i < right; i++)
		res = min(res, solve(left, i) + solve(i + 1, right));
	return res += sum[right] - sum[left - 1];
}

int main()
{
	ios_base::sync_with_stdio(NULL);
	cin.tie(NULL);
	cout.tie(NULL);
	
	int t, n;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		for (int k = 0; k < 501; k++)
			for (int p = 0; p < 501; p++)
				dp[k][p] = -1;
		cin >> n;
		for (int j = 1; j <= n; j++)
		{
			cin >> m[j];
			sum[j] = sum[j - 1] + m[j];
		}
		cout << solve(1, n) << "\n";
	}
	return 0;
}