#include <iostream>
using namespace std;

int Direction(char d) {
	if (d == 'U')
		return 3;
	if (d == 'D')
		return 1;
	if (d == 'R')
		return 0;
	if (d == 'L')
		return 2;
}

bool in_range(int x, int y, int n) {
	return (x > 0 && x <= n && y > 0 && y <= n);
}

int main(void)
{
	int n, t, r, c, dir;
	int dx[4] = { 0, 1, 0, -1 }, dy[4] = { 1, 0, -1, 0 }; 
	int arr[51][51];
	char d;
	cin >> n >> t;
	cin >> r >> c >> d;
	dir = Direction(d);

	for (int i = 0; i < t; i++) {
		if (in_range(r + dx[dir], c + dy[dir], n)) {
			r += dx[dir];
			c += dy[dir];
		}
		else {
			dir = (dir + 2) % 4;
		}
	}

	cout << r << ' ' << c;
	return 0;
}