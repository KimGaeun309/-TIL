#include <iostream>
using namespace std;

int main(void) {
	int num;
	cin >> num;
	int new_num = 0;
	while (1) {
		if (num == 0)
			break;
		new_num = (new_num * 10) + num % 10;
		num /= 10;
	}
	cout << new_num;
	return 0;
}
