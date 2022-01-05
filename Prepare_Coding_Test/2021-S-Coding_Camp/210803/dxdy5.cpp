#include <iostream>
using namespace std;

bool in_range(int x, int y, int n, int m) {
	return (x >= 0 && x < n && y >= 0 && y < m);
}

int main(void)
{
	int n, m, x = 0, y = -1, nx, ny, dir = 0;
	int dx[4] = { 0, 1, 0, -1 }, dy[4] = { 1, 0, -1, 0 };
	int arr[100][100] = { 0 };
	cin >> n >> m;

	for (int i = 1; i <= n * m; i++) {
		nx = x + dx[dir];
		ny = y + dy[dir];
		if (in_range(nx, ny, n, m) == false || (arr[nx][ny] != 0))
			dir = (dir + 1) % 4;
		x = x + dx[dir];
		y = y + dy[dir];
		arr[x][y] = i;
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cout << arr[i][j] << ' ';
		}
		cout << endl;
	}
	return 0;
}