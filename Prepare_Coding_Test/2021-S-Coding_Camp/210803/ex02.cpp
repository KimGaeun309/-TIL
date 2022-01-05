#include <iostream>
#include <limits>
using namespace std;

int main(void) {
	int n;
	int cnt = 0;
	cin >> n;
	int min = INT_MAX;
	for (int i = 0; i < n; i++) {
		int curr;
		cin >> curr;
		if (min > curr) {
			cnt = 1;
			min = curr;
		}
		else if (min == curr) {
			cnt++;
		}
	}

	cout << min << " " << cnt;
	return 0;
}