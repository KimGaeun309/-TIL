#include <iostream>
#include <string>
using namespace std;

int main(void) 
{
	string input_str;
	string goal_str;

	cin >> input_str;
	cin >> goal_str;

	for (int i = 0; i <= (input_str.length() - goal_str.length()); i++) {
		for (int j = 0; j < goal_str.length(); j++) {
			if (input_str[i + j] != goal_str[j])
				break;
			else if (j == goal_str.length() - 1) {
				cout << i;
				return 0;
			}
		}
	}

	cout << -1;
	return 0;

}