#include <iostream>
using namespace std;

int main(void)
{
	int n, m, k;
	int arr[100][100];
	bool check;
	int answer = 0;
	cin >> n >> m;
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			cin >> arr[i][j];

	
	for (int i = 0; i < n; i++) {
		check = false;
		for (int j = 0; j < (n - m + 1); j++) {
			// 가로 찾기
			for (k = 1; k < m; k++) {
				if (arr[i][j] != arr[i][j + k])
					break;
				
			}
			if (k == m)
				check = true;
		}
		if (check)
			answer++;
	}
	
	for (int j = 0; j < n; j++) {
		check = false;
		for (int i = 0; i < (n - m + 1); i++) {
			// 세로 찾기
			for (k = 0; k < m; k++) {
				if (arr[i][j] != arr[i + k][j])
					break;
			}
			if (k == m)
				check = true;
		}
		if (check)
			answer++;
	}


	cout << answer;
	return 0;
}