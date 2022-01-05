#include <iostream>
using namespace std;

bool in_range(int x, int y, int n) {
	return (x >= 0 && x < n&& y >= 0 && y < n);
}

int main(void)
{
	int n, nx, ny, dir;
	int dx[4] = {0, 1, 0, -1}, dy[4] = {1, 0, -1, 0};
	int arr[100][100];
	int cnt = 0, answer = 0;

	cin >> n;
	for (int x = 0; x < n; x++) 
		for (int y = 0; y < n; y++) 
			cin >> arr[x][y];

	for (int x = 0; x < n; x++) {
		for (int y = 0; y < n; y++) {
			cnt = 0;
			for (dir = 0; dir < 4; dir++) {
				nx = x + dx[dir];
				ny = y + dy[dir];
				if ((in_range(nx, ny, n)) && (arr[nx][ny] == 1))
					cnt++;
			}
			if (cnt >= 3)
				answer++;
		}
	}
	
	cout << answer;
	return 0;
}