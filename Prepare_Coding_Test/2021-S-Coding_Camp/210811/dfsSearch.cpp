#include <iostream>
#include <vector>;
using namespace std;
int n, m;
vector<int> graph[1001];
bool visited[1001];
int cnt = 0;

int dfsCount(int vertex) {
	for (int i = 0; i < graph[vertex].size(); i++) {
		int curr_v = graph[vertex][i];
		if (!visited[curr_v]) {
			cnt++;
			visited[curr_v] = true;
			dfsCount(curr_v);
		}
	}
	return cnt;
}

int main(void)
{
	cin >> n >> m;

	for (int i = 1; i <= m; i++) {
		int x, y;
		cin >> x >> y;
		graph[x].push_back(y);
		graph[y].push_back(x);
	}

	visited[1] = true;

	cout << dfsCount(1) << endl;
	return 0;
}

