#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

int dp[251][251 * 251];
int a[251], b[251];
int MAX = 978654321;
int main()
{
	ios_base::sync_with_stdio(NULL);
	cin.tie(NULL);
	cout.tie(NULL);

	int n;
	cin >> n;
	int mm = 0;
	for (int i = 1; i <= n; i++)
	{
		cin >> a[i] >> b[i];
		mm += a[i];
	}
	memset(dp, MAX, sizeof(dp));
	dp[1][mm] = 0;
	dp[1][mm - a[1]] = b[1];
	for (int i = 1; i < n; i++)
	{
		for (int j = 1; j <= mm; j++)
		{
			if (dp[i][j] != MAX)
			{
				dp[i + 1][j] = dp[i][j];
				dp[i + 1][j - a[i + 1]] = min(dp[i + 1][j - a[i + 1]], dp[i][j] + b[i + 1]);
			}
		}
	}
	int k = MAX;
	for (int i = 1; i <= mm; i++)
	{
		k = min(k, max(i, dp[n][i]));
	}
	cout << k;
	return 0;
}
