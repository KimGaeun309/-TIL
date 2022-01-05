#include <iostream>
using namespace std;

int main(void) {
	int n;
	int DP[50];
	cin >> n;

	DP[1] = 1;
	DP[2] = 1;

	for (int i = 3; i <= n; i++)
		DP[i] = DP[i - 1] + DP[i - 2];

	cout << DP[n] << endl;
	return 0;
}