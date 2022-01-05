#include <iostream>
using namespace std;

bool able(int x, int y, int n) {
	if (x < 0 || x >= n || y < 0 || y >= n)
		return false;
	return true;
}

bool change(int x, int y, int mid) {
	if ((mid - x) + (mid - y) == 0)
		return true;
	if ((mid - x) - (mid - y) == 0 && x < mid)
		return true;
	if ((mid - x) - (mid + 1 - y) == 0 && x >= mid)
		return true;
	return false;
}

int main(void) {
	int n;
	int square[100][100] = {0};
	cin >> n;

	int idx_x = n / 2;
	int idx_y = n / 2;
	int dx[4] = { 0, -1, 0, 1 }, dy[4] = { 1, 0, -1, 0 };
	int dir = -1;

	for (int i = 1; i <= n*n; i++) {

//		if (able(idx_x, idx_y, n) == false)
//			break;

		square[idx_x][idx_y] = i;

		// 다음 인덱스 지정
		if (change(idx_x, idx_y, n/2))
			dir = (dir+1) % 4;

		idx_x += dx[dir];
		idx_y += dy[dir];



	}
	
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cout << square[i][j] << ' ';
		}
		cout << endl;
	}
	return 0;

}