// �� Person()�� �Լ������� �̸� ����� �� �տ� new�� ���̸� ��ü�� return�ȴ�.
// new�� ���̸� Person()�� constructor�� �ȴ�.
// constructor�� ��ü�� ����� �� ��ü�� �ʱ� ���¸� �����ϴ� ������ �Ѵ�.
function Person(name, first, second, third) {
  this.name = name;
  this.first = first;
  this.second = second;
  this.third = third; // third �߰� (���� �۾�)
  // this.sum = function () {
  //   return this.first + this.second + this.third; // this ����� �ڽ��� ���� ��ü�� ����Ŵ
  // };
}

// prototype -> ���� ���� ��ü�� �� ���� �Լ��� ����
Person.prototype.sum = function () {
  return 'prototype : ' + (this.first + this.second + this.third);
};

var kim = new Person('kim', 10, 20, 30);
kim.sum = function () {
  // kim�� sum()�� ����
  return 'this : ' + (this.first + this.second);
};
// kim.sum = function () { // ��� ��ü�� sum �Լ��� �̷��� �ٲٷ��� �ϳ��ϳ� �����ؾ� ��
//   return 'modified : ' + (this.first + this.second + this.third);
// };
var lee = new Person('lee', 10, 10, 10);
// lee.sum = function () { // ��� ��ü�� sum �Լ��� �̷��� �ٲٷ��� �ϳ��ϳ� �����ؾ� ��
//   return 'modified : ' + (this.first + this.second + this.third);
// };
console.log('kim.sum()', kim.sum());
console.log('lee.sum()', lee.sum());

// -> prototype ����� �ذ�
