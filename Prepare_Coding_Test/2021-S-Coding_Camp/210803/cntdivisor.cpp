#include <iostream>
using namespace std;

int main(void) {
	int answer = 0; 
	int s, e;
	cin >> s >> e;

	for (int i = s; i <= e; i++) {
		int cnt = 0;
		for (int j = i; j > 0; j--) {
			if (i % j == 0)
				cnt++;
		}
		if (cnt == 3)
			answer += 1;
	}
	cout << answer;
	return 0;
}