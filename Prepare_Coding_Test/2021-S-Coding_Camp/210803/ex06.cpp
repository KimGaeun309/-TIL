#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Student
{
public:
	int height;
	int weight;
	int number;
	Student(int height, int weight, int number) {
		this->height = height;
		this->weight = weight;
		this->number = number;
	}
};

bool cmp(const Student& a, const Student& b) {
	if (a.height != b.height)
		return a.height > b.height;
	if (a.weight != b.weight) 
		return a.weight > b.weight;
	return a.number < b.number;
}

int main(void) {
	int n;
	cin >> n;
	vector<Student> students;
	for (int i = 1; i <= n; i++) {
		int a, b;
		cin >> a >> b;
		students.push_back(Student(a, b, i));
	}

	sort(students.begin(), students.end(), cmp);

	for (int i = 0; i < n; i++) {
		cout << students[i].height << " ";
		cout << students[i].weight << " ";
		cout << students[i].number << endl;
	}

	return 0;
}



