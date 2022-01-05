#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main(void)
{
	string input_str;
	cin >> input_str;
	int q_n;
	cin >> q_n;

	int q_arr[1000];

	for (int i = 0; i < q_n; i++) {
		int curr;
		cin >> curr;
		q_arr[i] = curr;
	}

	for (int i = 0; i < q_n; i++) {
		int q = q_arr[i];
		if (q == 1) {
			char tmp = input_str[0];
			for (int i = 0; i < input_str.length() - 1; i++)
				input_str[i] = input_str[i + 1];
			input_str[input_str.length() - 1] = tmp;
			
		}
		else if (q == 2) {
			char tmp = input_str[input_str.length() - 1];
			for (int i = input_str.length() - 1; i > 0 ; i--)
				input_str[i] = input_str[i-1];
			input_str[0] = tmp;
			
		}
		else if (q == 3) {
			reverse(input_str.begin(), input_str.end());
		}
		cout << input_str << endl;
	}
	
	return 0;
}
