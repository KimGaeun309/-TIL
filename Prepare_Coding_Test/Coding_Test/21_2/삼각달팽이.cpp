// 프로그래머스 2단계 삼각달팽이

#include <string>
#include <vector>
int grid[1000][1000] = { 0 };

using namespace std;

// 영역을 벗어나거나 이미 숫자가 채워진 위치인지 확인
bool inRange(int x, int y, int n) {
    if (x < 0 || x >= n || y < 0 || y >= n || grid[x][y] != 0)
        return false;
    return true;
}

vector<int> solution(int n) {
    vector<int> answer;

    int dx[3] = { 1, 0, -1 }, dy[3] = {0, 1, -1};
    int dir = 0;
    int num = 1;

    int lastNum = (n * n + n) / 2; // 가장 마지막으로 채워질 숫자
    
    // grid 에 차례대로 숫자 채우기
    for (int x = 0, y = 0; num <= lastNum; x = x + dx[dir], y = y + dy[dir]) {
        grid[x][y] = num++;

        if (!inRange(x + dx[dir], y + dy[dir], n))
            dir = (dir + 1) % 3;
    }
    
    for (int i = 0; i < n; i++)
        for (int j = 0; j <= i; j++)
            answer.push_back(grid[i][j]);

    return answer;
}
