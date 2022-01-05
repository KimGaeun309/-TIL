#include <iostream>
#include <climits>
#include <algorithm>
using namespace std;
int n, answer;
int arr[1001];
int dp[1001];

void Initialize() {
	for (int i = 0; i <= n; i++)
		dp[i] = INT_MAX;

	dp[0] = 0;
	arr[0] = 0;
}

int main(void)
{
	cin >> n;
	for (int i = 0; i < n; i++)
		cin >> arr[i];

	Initialize();

	for (int i = 1; i <= n; i++) {
		for (int j = 0; j < i; j++) {
			if (dp[j] == INT_MIN)
				continue;
			if (arr[j] < arr[i])
				dp[i] = max(dp[i], dp[j] + 1);
				
		}
	}


	for (int i = 0; i <= n; i++)
		answer = max(answer, dp[i]);
}

