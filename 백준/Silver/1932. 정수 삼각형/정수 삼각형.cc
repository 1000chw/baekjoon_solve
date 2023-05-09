#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
	int ar[501][501] = { 0, };
	int n, res = 0;
	cin >> n;
	for (int i = 1; i <= n; i++)
	{
		for (int j = 1; j <= i; j++)
		{
			cin >> ar[i][j];
		}
	}
	for (int i = 1; i <= n; i++)
	{
		for (int j = 1; j <= i; j++)
		{
			ar[i][j] += max(ar[i - 1][j - 1], ar[i - 1][j]);
		}
	}
	for (int i = 0; i <= n; i++)
	{
		if (ar[n][i] > res)
			res = ar[n][i];
	}
	cout << res << endl;
	return 0;
}