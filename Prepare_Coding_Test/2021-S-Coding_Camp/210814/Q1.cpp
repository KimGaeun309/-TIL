#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main(void)
{
	int arr[10];
	vector<int> big;
	vector<int> small;
	for (int i = 0; i < 10; i++) 
		cin >> arr[i];
			
	for (int i = 0; i < 10; i++) {
		if (arr[i] > 500)
			big.push_back(arr[i]);
		else
			small.push_back(arr[i]);
	}

	int min_num = big[0];
	int max_num = small[0];

	for (int i = 1; i < big.size(); i++) {
		if (big[i] < min_num)
			min_num = big[i];
	}

	for (int i = 1; i < small.size(); i++) {
		if (small[i] > max_num)
			max_num = small[i];
	}

	cout << max_num << ' ' << min_num;
	return 0;
}
