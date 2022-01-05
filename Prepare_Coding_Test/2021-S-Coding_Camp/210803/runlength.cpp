#include <iostream>
#include <string>
using namespace std;

int main(void)
{
	string A;
	string B = "";
	cin >> A;
	char curr_al = A[0];
	int curr_cnt = 0;
	int idx = 0;
	for (int i = 0; i < A.length(); i++) {
		if (A[i] == curr_al) {
			curr_cnt++;
			
		}
		else {
			B = B + curr_al + to_string(curr_cnt);
			curr_al = A[i];
			curr_cnt = 1;
		}
		if (i == A.length() - 1) {
			B = B + curr_al + to_string(curr_cnt);
		}
	}

	cout << B.length() << endl;
	cout << B;
	return 0;
}
