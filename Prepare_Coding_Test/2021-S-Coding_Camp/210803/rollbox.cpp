#include <iostream>
using namespace std;

int main(void)
{
	int n;
	int arr[200][200];
	
	cin >> n;
	for (int i = 0; i < n; i++) 
		for (int j = 0; j < n; j++) 
			cin >> arr[j][n-1-i];
		
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cout << arr[i][j] << " ";
		}
		cout << endl;
	}
	return 0;


}