#include <iostream>
#include <vector>
using namespace std;
int arr[21][21];
int n;
vector<int> s;

int WorkCal(int i, int j) {
	return (arr[i][j] + arr[j][i]);
}



int main(void)
{
	int morning, afternoon;
	int min;
	cin >> n;
	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= n; j++)
			cin >> arr[i][j];






}
