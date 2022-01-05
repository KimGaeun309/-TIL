#include <iostream>
using namespace std;

bool in_range(int r, int c, int n) {
	return (r >= 0 && r < n&& c >= 0 && c < n);
}

int main(void) {
	int n;
	int r, c, nr, nc;
	int dx[4] = {-1, 1, 0, 0}, dy[4] = {0, 0, -1 ,1};
	int arr[100][100];

	cin >> n >> r >> c;
	r = r - 1;
	c = c - 1;
	for (int i = 0; i < n; i++) 
		for (int j = 0; j < n; j++)
			cin >> arr[i][j];
	cout << arr[r][c] << ' ';
	while (1) {
		for (int i = 0; i < 4; i++) {
			
			nr = r + dx[i];
			nc = c + dy[i];
			if ( (in_range(nr, nc, n)) && (arr[r][c] < arr[nr][nc]) ) {
				r = nr;
				c = nc;
				cout << arr[r][c] << ' ';
				break;
			}
			if (i == 3)
				return 0;
		}

	}
}