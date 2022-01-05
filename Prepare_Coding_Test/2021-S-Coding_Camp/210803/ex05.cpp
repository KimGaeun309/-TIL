#include <iostream>
#include <algorithm>
using namespace std;

int main(void) {
	int n, k;
	cin >> n >> k;
	int arr[1000];
	for (int i = 0; i < n; i++)
	{
		int curr;
		cin >> curr;
		arr[i] = curr;
	}

	sort(arr, arr + n);
	cout << arr[k - 1];
}