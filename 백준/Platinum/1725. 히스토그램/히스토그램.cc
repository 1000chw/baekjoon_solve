#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<long long> vec;

long long solve(int left, int right)
{
	if (left == right)
		return vec[left];
	int mid = (left + right) / 2;
	long long res = max(solve(left, mid), solve(mid + 1, right));
	int low = mid, high = mid + 1;
	long long minH = min(vec[low], vec[high]);
	res = max(res, minH * 2);
	while (left < low || high < right)
	{
		if (high < right && (left == low || vec[low - 1] < vec[high + 1]))
		{
			high++;
			minH = min(minH, vec[high]);
		}
		else
		{
			low--;
			minH = min(minH, vec[low]);
		}
		res = max(res, minH * (high - low + 1));
	}
	return res;
}

int main()
{
	int n, num;
    vec.clear();
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        cin >> num;
        vec.push_back(num);
    }
    cout << solve(0, n - 1) << "\n";
	return 0;
}