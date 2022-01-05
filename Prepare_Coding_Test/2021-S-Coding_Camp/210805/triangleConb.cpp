#include <iostream>
using namespace std;

int UL[200], UR[200], D[200];

void TriRotate(int n) {
	int tmp = D[n - 1];

	for (int i = n - 1; i > 0; i--)
		D[i] = D[i - 1];
	D[0] = UR[n - 1];

	for (int i = n - 1; i > 0; i--)
		UR[i] = UR[i - 1];
	UR[0] = UL[n - 1];

	for (int i = n - 1; i > 0; i--)
		UL[i] = UL[i - 1];
	UL[0] = tmp;
}

int main(void) {
	int n, t;
	
	cin >> n >> t;

	for (int i = 0; i < n; i++)
		cin >> UL[i];
	for (int i = 0; i < n; i++)
		cin >> UR[i];
	for (int i = 0; i < n; i++)
		cin >> D[i];

	for (int i = 0; i < t; i++)
		TriRotate(n);

	for (int i = 0; i < n; i++)
		cout << UL[i] << ' ';
	cout << endl;

	for (int i = 0; i < n; i++)
		cout << UR[i] << ' ';
	cout << endl;

	for (int i = 0; i < n; i++)
		cout << D[i] << ' ';
	cout << endl;
	return  0;
}
