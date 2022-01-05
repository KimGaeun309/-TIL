#include <iostream>
using namespace std;

int main(void)
{
	int n, m;
	int arr[100][100];
	int idx_i = -1, idx_j = 1, cnt_j = 0, cnt_i = 0;
	cin >> n >> m;
	
	for (int i = 1; i <= n * m; i++) {
		// ÀÎµ¦½º ¹üÀ§¸¦ ¹þ¾î³ª¸é
		if (idx_i + 1 >= n || idx_j - 1 < 0) {
			if (cnt_j + 1 < m)
				arr[idx_i = 0][idx_j = ++cnt_j] = i;
			else
				arr[idx_i = ++cnt_i][idx_j = m - 1] = i;
		}
		else {
			 arr[++idx_i][--idx_j] = i;
		}
	}
	
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cout << arr[i][j] << " ";
		}
		cout << endl;
	}
	return 0;
}