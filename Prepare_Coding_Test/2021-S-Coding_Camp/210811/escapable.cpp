#include <iostream>
using namespace std;
int n, m;
int grid[100][100];
bool visited[100][100];

bool CanGo(int x, int y) {
	if (x < 0 || x >= n || y < 0 || y >= m)
		return false;
	if (visited[x][y] || grid[x][y] == 0)
		return false;
	return true;
}

void DFS(int x, int y) {
	int dx[2] = { 1, 0 }, dy[2] = { 0, 1 };

	for (int i = 0; i < 2; i++) {
		int nx = x + dx[i];
		int ny = y + dy[i];

		if (CanGo(nx, ny)) {
			visited[nx][ny] = true;
			DFS(nx, ny);
		}
	}
}

int main(void)
{
	cin >> n >> m;

	for (int i = 0; i < n; i++) 
		for (int j = 0; j < m; j++)
			cin >> grid[i][j];

	visited[0][0] = true;
	DFS(0, 0);

	cout << visited[n - 1][m - 1];
	return 0;
}