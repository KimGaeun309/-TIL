#include <iostream>
using namespace std;
int arr[101];
int end_of_arr;
int temp[101];
int end_of_temp;

void Delete(int s, int e) {
	end_of_temp = 0;
	for (int i = 1; i <= end_of_arr; i++) {
		if (i >= s && i <= e)
			continue;
		end_of_temp++;
		temp[end_of_temp] = arr[i];
		
	}

	for (int i = 1; i <= end_of_temp; i++) {
		arr[i] = temp[i];
	}
	end_of_arr = end_of_temp;
}

int main(void)
{
	int n, s1, s2, e1, e2;

	cin >> n;
	for (int i = 1; i <= n; i++)
		cin >> arr[i];
	cin >> s1 >> e1;
	cin >> s2 >> e2;
	end_of_arr = n;

	Delete(s1, e1);
	Delete(s2, e2);

	cout << end_of_arr << endl;

	for (int i = 1; i <= end_of_arr; i++)
		cout << arr[i] << endl;
	return 0;
}