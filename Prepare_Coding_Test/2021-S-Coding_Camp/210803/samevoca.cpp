#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main(void) {
	string A, B;
	cin >> A >> B;

	if (A.length() != B.length()) {
		cout << "No";
		return 0;
	}
	
	sort(A.begin(), A.end());
	sort(B.begin(), B.end());

	for (int i = 0; i < A.length() ; i++) {
		if (A[i] != B[i]) {
			cout << "No";
			return 0;
		}
	}
	cout << "Yes";
	return 0;
}