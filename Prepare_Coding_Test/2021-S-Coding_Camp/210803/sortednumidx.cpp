#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Number {
public:
	int num;
	int idx;

	Number(int num, int idx) {
		this->num = num;
		this->idx = idx;
	}

};

bool cmp(const Number& a, const Number& b) {
	if (a.num != b.num)
		return a.num < b.num;
	return a.idx < b.idx;
}

int main(void) {
	int n;
	int num;
	int arr[1000];
	vector<Number> numbers;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> num;
		numbers.push_back(Number(num, i));
	}

	sort(numbers.begin(), numbers.end(), cmp);

	// 정답 저장
	for (int i = 0; i < n; i++) {
		arr[numbers[i].idx] = i + 1;
	}

	for (int i = 0; i < n; i++) {
		cout << arr[i] << ' ';
	}
	return 0;
}