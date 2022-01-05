/*
보고 말하는 수열
보고 말하는 수열이란 다음 규칙을 만족하는 수열입니다.

수열의 첫 번째 원소는 1 입니다.

수열의 N 번째 원소는 N - 1번째 원소에 “보고 말하는” 과정을 거쳐 완성됩니다.

첫 번째 원소 1은 ‘1이 1개 있다’고 말할 수 있으므로, 두 번째 원소는 11이 됩니다.

두 번째 원소 11은 ‘1이 2개 있다’고 말할 수 있으므로, 세 번째 원소는 12가 됩니다.

세 번째 원소 12는 ‘1이 1개, 2가 1개 있다’고 말할 수 있으므로, 네 번째 원소는 1121가 됩니다.

네 번째 원소 1121는 ‘1이 2개, 2가 1개, 1이 1개 있다’고 말할 수 있으므로, 다섯 번째 원소는 122111이 됩니다.

위와 같이 순서대로 같은 숫자가 나오지 않는 순간을 기준으로 끊어 해당 숫자와 연속하여 나온 개수를 연달아 적은 결과가 그 다음 원소가 됩니다.

보고 말하는 수열의 N번째 원소를 구하는 프로그램을 작성해보세요.

입력 형식
N이 주어집니다.

1 ≤ N ≤ 20
출력 형식
보고 말하는 수열의 N번째 원소를 출력하세요. 출력 결과가 1000자리를 넘지 않는다고 가정해도 좋습니다.

입출력 예제
예제1
입력:
2

출력:
11
예제2
입력:
5

출력:
122111
*/


#include <iostream>
#include <vector>
using namespace std;

int main(void) {
	int n;
	vector<int> numbers[21];xdy1.cpp

	cin >> n;

	numbers[1].push_back(1);

	for (int i = 1; i < n; i++) {
		int cnt = 1;
		for (int j = 1; j <= (int)numbers[i].size(); j++) {
			if (j == (int)numbers[i].size() ||  numbers[i][j - 1] != numbers[i][j] ) {
				numbers[i+1].push_back(numbers[i][j - 1]);
				numbers[i+1].push_back(cnt);
				cnt = 1;
			}
			else
				cnt++;
		}
	}

	for (int j = 0; j < (int)numbers[n].size(); j++) {
		cout << numbers[n][j];
	}
		
	return 0;
}