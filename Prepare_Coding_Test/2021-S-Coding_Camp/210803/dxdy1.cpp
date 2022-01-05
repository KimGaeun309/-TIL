#include <iostream>
using namespace std;

int Direction(char d) {
	if (d == 'W')
		return 0;
	if (d == 'S')
		return 1;
	if (d == 'N')
		return 2;
	if (d == 'E')
		return 3;
}

int main(void) {
	int n, num, x = 0, y = 0, dir;
	char d;
	cin >> n;

	int dx[4] = { -1, 0, 0, 1 }, dy[4] = { 0, -1, 1, 0 };

	for (int i = 0; i < n; i++) {
		cin >> d >> num;
		dir = Direction(d);
		for (int j = 0; j < num; j++) {
			x += dx[dir];
			y += dy[dir];
		}
	}

	cout << x << ' ' << y << endl;
	return 0;
}