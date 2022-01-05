#include <iostream>
using namespace std;

int main(void)
{
	int n, t;
	int U[200], D[200];
	cin >> n >> t;

	for (int i = 0; i < n; i++) 
		cin >> U[i];

	for (int i = 0; i < n; i++)
		cin >> D[i];

	while (t-- > 0) {
		// U 옮기기
		int tmp = U[n-1];
		for (int j = n - 1; j >= 1; j--)
			U[j] = U[j - 1];

		// D 옮기기
		U[0] = D[n-1];
		for (int j = n - 1; j >= 1; j--)
			D[j] = D[j - 1];
		D[0] = tmp;
	}

	for (int i = 0; i < n; i++)
		cout << U[i] << ' ';
	cout << endl;
	for (int i = 0; i < n; i++)
		cout << D[i] << ' ';
	cout << endl;
	return 0;
}