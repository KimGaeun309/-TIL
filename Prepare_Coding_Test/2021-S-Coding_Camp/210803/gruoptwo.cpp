#include <iostream>
#include <algorithm>
using namespace std;

int main(void) {
	int n, max;
	int arr[2000];

	cin >> n;

	for (int i = 0; i < 2 * n; i++)
		cin >> arr[i];

	sort(arr, arr + 2 * n);
	max = arr[0] + arr[2 * n - 1];
	for (int i = 1; i < n; i++) {
		int tmp = arr[i] + arr[2 * n - 1 - i];
		if (tmp > max)
			max = tmp;
	}
	cout << max;
	return 0;

}
