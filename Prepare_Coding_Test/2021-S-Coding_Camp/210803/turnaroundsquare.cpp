#include <iostream>
using namespace std;

int able(int x, int y, int n, int m, char(&arr)[100][100]) {
	if (x < 0 || x >= n || y < 0 || y >= m)
		return -1;
	if (arr[x][y] != NULL)
		return -1;
	return 0;
}

int main(void) {
	char square[100][100] = { '\0' };
	int n, m;
	char alphabet = 'A';
	int dx[4] = { 0, 1, 0, -1 }, dy[4] = { 1, 0, -1, 0 };
	int dir = 0;
	int idx_x = 0, idx_y = -1;
	cin >> n >> m;
	
	for (int r = 0; r < n * m; r++) {
		
		switch (able(idx_x + dx[dir], idx_y + dy[dir], n, m, square)) {
		case -1:
			if (dir + 1 >= 4)
				dir = 0;
			else
				dir++;
		case 0:
			idx_x += dx[dir];
			idx_y += dy[dir];
			square[idx_x][idx_y] = alphabet;
			break;
		}

		if (alphabet == 'Z')
			alphabet = 'A';
		else
			alphabet++;

	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cout << square[i][j] << ' ';
		}
		cout << endl;
	}
	return 0;

	
}