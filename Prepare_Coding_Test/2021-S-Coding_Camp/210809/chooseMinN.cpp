#include <iostream>
#include <vector>
using namespace std;
int n, m;
vector<int> combination;

void PrintCombination() {
	for (int i = 0; i < m; i++)
		cout << combination[i] << ' ';
	cout << endl;
}

void FindCombination(int curr_num, int cnt) {
	if (curr_num > n) {
		if (cnt == m)
			PrintCombination();
		return;
	}

	// 선택함
	combination.push_back(curr_num);
	FindCombination(curr_num + 1, cnt + 1);
	combination.pop_back();

	// 선택 안함
	FindCombination(curr_num + 1, cnt);
}

int main(void)
{
	cin >> n >> m;
	FindCombination(1, 0);
	return 0;
}