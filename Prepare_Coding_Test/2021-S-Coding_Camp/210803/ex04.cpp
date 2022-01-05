#include <iostream>
using namespace std;

int main() {
	int n, m;
	cin >> n >> m;
	int grid[100][100];
	int cnt = 0;
	for (int j = 0; j < m; j++) {
		if (j % 2 == 0) {
			for (int i = 0; i < n; i++) {
				grid[i][j] = cnt++;
			}
		}
		else {
			for (int i = (n - 1); i >= 0; i--) {
				grid[i][j] = cnt++;
			}
		}
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cout << grid[i][j] << " ";
		}
		cout << endl;
	}

}