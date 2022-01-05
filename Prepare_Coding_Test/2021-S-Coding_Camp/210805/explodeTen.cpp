#include <iostream>
using namespace std;
int n;
int grid[201][201];

bool InRange(int x, int y) {
	return x > 0 && x <= n && y > 0 && y <= n;
}

void Pop(int r, int c) {
	int dx[4] = { 1, -1, 0, 0 }, dy[4] = { 0, 0, 1, -1 };
	for (int dir = 0; dir < 4; dir++) {
		int nr = r, nc = c;
		for (int i = 1; i < grid[r][c]; i++) {
			nr = nr + dx[dir];
			nc = nc + dy[dir];
			if (InRange(nr, nc)) {
				grid[nr][nc] = 0;
			}
			else
				break;
		}
	}
	grid[r][c] = 0;
}

void Fall() {
	int Temp[201][201] = { 0 };
	for (int j = 1; j <= n; j++) {
		int tmp_idx = n;
		for (int i = n; i > 0; i--) {
			if (grid[i][j] != 0) {
				Temp[tmp_idx--][j] = grid[i][j];
			}
		}
	}

	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++)
			grid[i][j] = Temp[i][j];
	}
}

int main(void)
{
	int r, c;
	cin >> n;
	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= n; j++)
			cin >> grid[i][j];
	cin >> r >> c;

	Pop(r, c);
	Fall();

	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++)
			cout << grid[i][j] << ' ';
		cout << endl;
	}

	return 0;
}