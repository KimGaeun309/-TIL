#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Point {
public:
	int x, y, num;
	int dist;
	Point(int x, int y, int num) {
		this->x = x; 
		this->y = y;
		this->num = num;
		this->dist = (x > 0 ? x : -x) + (y > 0 ? y : -y);
	}
};

bool cmp(const Point& a, const Point& b) {
	if (a.dist != b.dist)
		return a.dist < b.dist;
	return a.num < b.num;
}

int main(void) {
	int n, x, y;
	vector<Point> points;
	cin >> n;

	for (int i = 1; i <= n; i++) {
		cin >> x >> y;
		points.push_back(Point(x, y, i));
	}

	sort(points.begin(), points.end(), cmp);

	for (int i = 0; i < n; i++) {
		cout << points[i].num << endl;
	}
	return 0;
}