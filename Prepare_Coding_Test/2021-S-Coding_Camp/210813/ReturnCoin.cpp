#include <iostream>
#include <algorithm>
#include <climits>
using namespace std;
int n, m, answer;
int coin[101];
int dp[10001];

void Initialize() {
	for (int i = 0; i <= m; i++)
		dp[i] = INT_MAX;
}

int main(void)
{
	cin >> n >> m;

	for (int i = 1; i <= n; i++)
		cin >> coin[i];

	Initialize();

	for (int i = 1; i <= m; i++) {
		for (int j = 1; j <= n; j++) {
			if (dp[i - coin[j]] == INT_MAX)
				continue;
			if (i >= coin[j])
				dp[i] = min(dp[i], dp[i - coin[j]] + 1);
		}
	}

	answer = dp[m];

	if (answer == INT_MAX)
		answer = -1;

	cout << answer;
	return 0;
}