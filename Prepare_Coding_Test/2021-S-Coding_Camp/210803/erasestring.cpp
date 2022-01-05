#include <iostream>
#include <string>
using namespace std;

int main(void)
{
	string A, B;
	cin >> A >> B;
	if (A.length() < B.length()) {
		cout << A;
		return 0;
	}

	while (1) {
		bool change = false;
		for (int i = 0; i <= (A.length() - B.length()); i++) {
			
			for (int j = 0; j < B.length(); j++) {
				if (A[i + j] != B[j]) {
					break;
				}
				else if (j == B.length() - 1) {
					for (int k = i; k < A.length() - B.length(); k++) {
						A[k] = A[k + B.length()];
					}
					for (int k = A.length() - B.length(); k < A.length(); k++) {
						A[k] = NULL;
					}
					change = true;
					break;
				}
			}
			
		}
		if (change == false)
			break;

	}

	cout << A;
	return 0;
}