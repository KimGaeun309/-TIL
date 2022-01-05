#include <iostream>
using namespace std;

int Square[21][21];

int dx[4] = { -1, 1, 0, 0 }, dy[4] = { 0, 0, -1 ,1 };

bool in_range(int x, int y, int n) {
	return (x > 0 && x <= n && y > 0 && y <= n);
}

int find_dir(int x, int y, int n) {
	int d = 0, max = 0;
	int nx, ny;

	for (int i = 0; i < 4; i++) {
		nx = x + dx[i];
		ny = y + dy[i];
		if ((in_range(nx, ny, n)) && (Square[nx][ny] > max)) {
			max = Square[x + dx[i]][y + dy[i]];
			d = i;
		}
	}
	return d;
}

int main(void)
{
	int n, m, t, r, c;
	int Count[21][21] = { 0 };
	int NewCount[21][21] = { 0 };
	int dir, answer = 0;

	// 입력받기
	cin >> n >> m >> t;
	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= n; j++)
			cin >> Square[i][j];
	for (int i = 1; i <= m; i++) {
		cin >> r >> c;
		Count[r][c] = 1;
	}

	// t 시간동안
	while (t--) {

		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= n; j++) {
				// 구슬 옮겨주기
				if (Count[i][j] == 1) {
					dir = find_dir(i, j, n);
					NewCount[i + dx[dir]][j + dy[dir]]++;
				}
			}
		}
		// Count로 옮기고 NewCount 초기화
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= n; j++) {
				if (NewCount[i][j] == 1)
					Count[i][j] = 1;
				else
					Count[i][j] = 0;
				NewCount[i][j] = 0;
			}
		}
	}

	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= n; j++)
			if (Count[i][j] == 1)
				answer++;

	cout << answer;
	return 0;
}