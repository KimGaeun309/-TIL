#include <iostream>
using namespace std;
int n, m;
int grid[100][100];

bool InRange(int x, int y) {
	return x >= 0 && x < n&& y >= 0 && y < n;
}

void SWAP(int x, int y) {
	int ans_dir = 0, tmp;
	int dx[8] = { -1, -1, -1, 0, 1, 1, 1, 0 };
	int dy[8] = { -1, 0, 1, 1, 1, 0, -1, -1 };
	int max = grid[x + dx[0]][y + dy[0]];
	for (int dir = 1; dir < 8; dir++) {
		int nx = x + dx[dir];
		int ny = y + dy[dir];

		if (InRange(nx, ny) && grid[nx][ny] > max) {
			max = grid[nx][ny];
			ans_dir = dir;
		}
	}

	tmp = grid[x][y];
	grid[x][y] = max;
	grid[x + dx[ans_dir]][y + dy[ans_dir]] = tmp;
}

void FindIdxAndChange(int num) {
	int x = 0;
	int y = 0;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (grid[i][j] == num) {
				x = i;
				y = j;
				break;
			}
		}
	}

	SWAP(x, y);
}

void MOVE() {
	for (int num = 1; num <= n * n; num++) {
		FindIdxAndChange(num);
	}
}

int main(void)
{
	cin >> n >> m;

	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			cin >> grid[i][j];

	for (int cnt = 0; cnt < m; cnt++)
		MOVE();


	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++)
			cout << grid[i][j] << ' ';
		cout << endl;
	}
	return 0;
}