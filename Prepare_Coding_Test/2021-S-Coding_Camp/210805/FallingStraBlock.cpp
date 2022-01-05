#include <iostream>
using namespace std;
int n;
int grid[101][101];

bool CanGo(int m, int r, int c) {
	if (r > n || r <= 0 || c <= 0 || m + c - 1 > n)
		return false;

	for (int j = c; j < (m + c); j++) {
		if (grid[r][j] != 0)
			return false;
	}
	return true;
}

void FallBlock(int m, int k) {
	for (int i = 1; i <= n+1; i++) {
		if (!CanGo(m, i, k)) {
			for (int j = k; j < m+k; j++)
				grid[i - 1][j] = 1;
			break;
		}
	}
}

int main(void)
{
	int m, k;
	cin >> n >> m >> k;

	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= n; j++)
			cin >> grid[i][j];

	FallBlock(m, k);

	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++)
			cout << grid[i][j] << ' ';
		cout << endl;
	}

	return 0;
}