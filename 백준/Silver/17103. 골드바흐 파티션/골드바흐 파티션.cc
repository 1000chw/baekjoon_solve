#include <iostream>
#include <cmath>
#include <cstring>
using namespace std;

bool prime_number[1000001];
int T;
int n;

int main() {
	memset(prime_number, true, sizeof(prime_number));
	for (int i = 2; i < 1000; i++)
	{
		if (prime_number[i] == true) {
			for (int j = 2; j <= 1000000/i; j++)
			{
				prime_number[i * j] = false;
			}
		}
	}
	cin >> T;
	for (int i = 0; i < T; i++) {
		cin >> n;
		int res = 0;
		for (int j = 2; j <= n/2; j++)
		{
			if (prime_number[j] && prime_number[n - j])
				res++;
		}
		cout << res << '\n';
	}
	
	return 0;
}
