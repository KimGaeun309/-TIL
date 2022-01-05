#include <iostream>
#include <vector>
using namespace std;
int k, n;
vector<int> answer;

void Choose(int curr_num) {
	// 출력
	if (curr_num > n) {
		for (int i = 0; i < n; i++)
			cout << answer[i] << ' ';
		cout << endl;
		return;
	}

	// 조합
	for (int i = 1; i <= k; i++) {
		answer.push_back(i);
		Choose(curr_num + 1);
		answer.pop_back();
	}

}

int main(void)
{
	cin >> k >> n;

	Choose(1);

	return 0;
}
