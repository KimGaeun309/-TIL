#include <iostream>
using namespace std;

int main(void)
{
	int n;
	
	int arr[100];
	cin >> n;

	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}

	for (int i = 0; i < n; i++) {
		int max = arr[i];
		int max_idx = i;
		for (int j = i; j < n; j++) {
			if (arr[j] >= max) {
				max = arr[j];
				max_idx = j;
			}
		}
		int tmp = arr[i];
		arr[i] = arr[max_idx];
		arr[max_idx] = tmp;
	}

	cout << arr[0] << " " << arr[1] << endl;
	return 0;


}
