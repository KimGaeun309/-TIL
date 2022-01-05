#include <iostream>
using namespace std;
int n, m, q;
int arr[101][101];

void Rotate(int r, char d) {
	if (d == 'L') { // 오른쪽 로테이션
		int tmp = arr[r][m];
		for (int i = m; i > 1; i--)
			arr[r][i] = arr[r][i - 1];
		arr[r][1] = tmp;
	}
	else if (d == 'R') { // 왼쪽 로테이션
		int tmp = arr[r][1];
		for (int i = 1; i < m; i++)
			arr[r][i] = arr[r][i + 1];
		arr[r][m] = tmp;
	}
}

bool IsMovable(int a, int b) {
	for (int i = 1; i <= m; i++) {
		if (arr[a][i] == arr[b][i])
			return true;
	}
	return false;
}

char Flip(char c) {
	if (c == 'L')
		return 'R';
	else
		return 'L';
}

void WindBlow(int r, char d) {
	Rotate(r, d);

	// 위로
	char dir = Flip(d);
	for (int row = r; row > 1; row--) {
		if (IsMovable(row, row - 1)) {
			Rotate(row - 1, dir);
			dir = Flip(dir);
		}
		else
			break;
	}

	// 아래로
	dir = Flip(d);
	for (int row = r; row < n; row++) {
		if (IsMovable(row, row + 1)) {
			Rotate(row + 1, dir);
			dir = Flip(dir);
		}
		else break;
	}
}

int main(void)
{
	cin >> n >> m >> q;
	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= m; j++)
			cin >> arr[i][j];
	for (int i = 0; i < q; i++) {
		int r;
		char d;
		cin >> r >> d;
		WindBlow(r, d);
	}

	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= m; j++)
			cout << arr[i][j] << " ";
		cout << endl;
	}
	return 0;
}
