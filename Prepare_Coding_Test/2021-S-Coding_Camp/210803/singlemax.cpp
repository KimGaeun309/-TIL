#include <iostream>
using namespace std;

int main(void)
{
	int n;
	int arr[1000];
	cin >> n;

	for (int i = 0; i < n; i++)
		cin >> arr[i];

	for (int i = 0; i < n - 1; i++) {
		int curr = arr[i];
		for (int j = i + 1; j < n; j++) {
			if (arr[j] == curr) {
				arr[i] = -1;
				arr[j] = -1;
			}
		}
	}

	int max = arr[0];
	for (int i = 0; i < n; i++) {
		if (arr[i] > max)
			max = arr[i];
	}
	cout << max;
	return 0;


}