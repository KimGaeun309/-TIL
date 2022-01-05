#include <iostream>
using namespace std;
int arr[20][20];

int GetNumOfGold(int r_s, int r_e, int c_s, int c_e) {
	int cnt = 0;
	for (int r = r_s; r <= r_e; r++) {
		for (int c = c_s; c <= c_e; c++) {
			cnt += arr[r][c];
		}
	}
	return cnt;
}



int main(void)
{
	int n;
	int max = 0;
	cin >> n;

	for (int i = 0; i < n; i++) 
		for (int j = 0; j < n; j++) 
			cin >> arr[i][j];

	for (int i = 0; i < (n - 2); i++) {
		for (int j = 0; j < (n - 2); j++) {
			int num_of_gold = GetNumOfGold(i, i+2, j, j + 2);
			if (max < num_of_gold)
				max = num_of_gold;
		}
	}
	cout << max;
	return 0;
}