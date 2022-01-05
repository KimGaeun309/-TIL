#include <iostream>
using namespace std;

int main(void) {
	int n, max_idx;
	int arr[1000];
	cin >> n;

	for (int i = 0; i < n; i++)
		cin >> arr[i];

	while (n != 0) {
		int max = arr[0];
		max_idx = 0;
		for (int i = 1; i < n; i++) {
			if (arr[i] > max) {
				max = arr[i];
				max_idx = i;
			}
			
		}
		cout << max_idx + 1 << " ";
		n = max_idx;
	}
	return 0;
}
