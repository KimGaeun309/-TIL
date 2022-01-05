#include <iostream>
#include <string>
using namespace std;

int main(void)
{
	string A;
	int dx[4] = { 0, 1, 0, -1 }, dy[4] = { 1, 0, -1, 0 };
	int x = 0, y = 0, dir = 0;
	cin >> A;

	
	for (int i = 0; i < A.length(); i++) {
		if (A[i] == 'L') {
			dir = (dir - 1 + 4) % 4;
		}
		else if (A[i] == 'R') {
			dir = (dir + 1) % 4;
		}
		else if (A[i] == 'F') {
			x += dx[dir];
			y += dy[dir];
		}
	}

	cout << x << ' ' << y << endl;
	return 0;
}