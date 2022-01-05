#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int dp[1001][1001];
string A, B;

void Initialize() {
	dp[1][1] = (A[1] == B[1]) ? 1 : 0;

	for (int i = 2; i < A.length(); i++) {
		if (A[i] == B[1])
			dp[i][1] = 1;
		else
			dp[i][1] = dp[i - 1][1];
	}

	for (int j = 2; j < B.length(); j++) {
		if (A[1] == B[j])
			dp[1][j] = 1;
		else
			dp[1][j] = dp[1][j - 1];
	}
}

int main(void)
{
	cin >> A >> B;

	A = "#" + A;
	B = "#" + B;

	Initialize();

	for (int i = 2; i < A.length(); i++) {
		for (int j = 2; j < B.length(); j++) {
			if (A[i] == B[j])
				dp[i][j] = dp[i - 1][j - 1] + 1;
			else
				dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
		}
	}

	cout << dp[A.length()-1][B.length()-1];
	return 0;
}