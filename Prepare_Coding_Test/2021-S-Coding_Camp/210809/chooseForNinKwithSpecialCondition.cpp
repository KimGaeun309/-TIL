#include <iostream>
#include <vector>
using namespace std;
int k, n;
vector<int> answer;

void Choose(int cnt)
{
	if (cnt == n) {
		for (int i = 0; i < n; i++)
			cout << answer[i] << ' ';
		cout << endl;
		return;
	}

	for (int i = 1; i <= k; i++) {
		if (cnt < 2 || !(answer[cnt-2] == answer[cnt-1] && answer[cnt-1] == i)) {
			answer.push_back(i);
			Choose(cnt + 1);
			answer.pop_back();
		}
	}
}

int main(void)
{
	cin >> k >> n;

	Choose(0);

	return 0;
}
