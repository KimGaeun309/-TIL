#include <iostream>
#include <algorithm>
using namespace std;

int main(void)
{
	int n;
	int arr[101][101];
	int sum[101][101];
	cin >> n;
	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= n; j++)
			cin >> arr[i][j];

	sum[1][1] = arr[1][1];
	for (int i = 2; i <= n; i++)
		sum[i][1] = sum[i - 1][1] + arr[i][1];
	for (int j = 2; j <= n; j++)
		sum[1][j] = sum[1][j - 1] + arr[1][j];

	for (int i = 2; i <= n; i++) 
		for (int j = 2; j <= n; j++) 
			sum[i][j] = max(sum[i - 1][j] + arr[i][j], sum[i][j - 1] + arr[i][j]);
		
	cout << sum[n][n];
	return 0;

}