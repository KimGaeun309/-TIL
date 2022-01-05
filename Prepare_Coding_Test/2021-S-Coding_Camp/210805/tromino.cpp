#include <iostream>
using namespace std;

bool in_range(int x, int y, int n, int m) {
	return (x >= 0 && x < n && y >= 0 && y < m);
}


int main(void)
{
	int n, m, max = 0;
	int dir1, dir2, nx1, ny1, nx2, ny2;
	int dx[4] = { 0, 1, 0, -1 }, dy[4] = { 1, 0, -1, 0 };
	int arr[200][200];
	cin >> n >> m;
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
			cin >>arr[i][j];

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			for (dir1 = 0; dir1 < 4; dir1++) {
				for (dir2 = 0; dir2 < 4; dir2++) {
					if (dir1 == dir2)
						break;
					// 세 값의 합의 최대 구하기
					nx1 = i + dx[dir1];
					ny1 = j + dy[dir1];
					nx2 = i + dx[dir2];
					ny2 = j + dy[dir2];

					if (in_range(nx1, ny1, n, m) && in_range(nx2, ny2, n, m) && (max < (arr[i][j] + arr[nx1][ny1] + arr[nx2][ny2])))
						max = arr[i][j] + arr[nx1][ny1] + arr[nx2][ny2];
				}
			}
		}
	}
	cout << max;
	return 0;
}
