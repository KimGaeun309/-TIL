#include <iostream>
using namespace std;

int main(void) {
	int answer = 0;
	int s, e;
	cin >> s >> e;

	for (int i = s; i <= e; i++) {
		int sum = 0;
		for (int j = i-1; j > 0; j--) {
			if (i % j == 0)
				sum += j;
		}
		if (sum == i)
			answer++;
	}
	cout << answer;
	return 0;
}