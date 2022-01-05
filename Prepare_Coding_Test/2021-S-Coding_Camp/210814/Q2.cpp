#include <iostream>
#include <algorithm>
using namespace std;
int n;
int arr[20][20];
bool visited[20][20];

bool CanGo(int i, int j) {
	if (i < 0 || i >= n || j < 0 || j + 2 >= n)
		return false;
	for (int col = j; col < j + 3; col++)
		if (visited[i][col] == true)
			return false;
	return true;
}

int GoldCount(int r, int col) {
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			visited[i][j] = false;
	int count = 0;

	for (int c = col; c < col + 3; c++) {
		count += arr[r][c];
		visited[r][c] = true;
	}

	int max_new_count = 0;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n - 2; j++) {
			int new_count = 0;
			if (!CanGo(i, j))
				continue;
			for (int k = j; k < j + 3; k++) {
				new_count += arr[i][k];
			}

			if (new_count > max_new_count)
				max_new_count = new_count;
		}
	}

	return count + max_new_count;
}

int main(void)
{
	int max_gold = 0;
	cin >> n;

	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			cin >> arr[i][j];

	for (int row = 0; row < n; row++) {
		for (int col = 0; col < n - 2; col++) {
			int cnt_gold = GoldCount(row, col);

			max_gold = max(max_gold, cnt_gold);
		}
	}
	cout << max_gold;
	return 0;
}