/* javascript�� ���� ������ �����ϴ� ��� �� �ϳ�.
  class�� java, python �� ���� ������ ��ü�� ����� �������� �����ߴµ�
  javascript�� �׷� ������ ���� �ʾҾ����� class�� �����ؼ� �̹� �ٸ� ��ǻ�� ���� ����ϴ� ��ü ������
  �����ϱ� ������. */

/* class�� ��ü�� ���� ����, construct function�� ��ü���� �� �� �ִ�.
  class�� ECMA script 6���� ���Ե� �����̴�.
  ���ó� ���� ����������� Node.js �� ���� �÷������� ECMA script 6 �̻��� ���� �����Ѵ�.
  javascript�� ���� ��ü ���� ����̹Ƿ� ���Ӱ� ���Ե� ������ �̹� �����ϴ� ��ɤ��� ������ ������, 
  ������ �������ε� ��Ÿ�� �� �ִ�. */

// prototype.js �� �Ȱ��� �����ϴ� ���� class�� ������.

class Person {
  //sum() {} // -> function �̶�� Ű���� ���� �Լ� ����
  constructor(name, first, second, third) {
    // ��ü�� ������ �� ����Ǵ� �Լ�!
    // constructor �Լ��� �ʱⰪ ���� ����.
    console.log('constructor');
    this.name = name;
    this.first = first;
    this.second = second;
    this.third = third;
  }
  // class�� �޼ҵ� �߰� ���2: ���ο� ����
  sum() {
    // �� �޼ҵ�� ��� ��ü�� �����
    return 'prototype : ' + (this.first + this.second + this.third);
  }
}

// class�� �޼ҵ� �߰� ��� 1: prototype �״�� ���
// Person.prototype.sum = function () {
//   return 'prototype : ' + (this.first + this.second + this.third);
// };

// ��ü�� �����ϰ� �ʱⰪ ����
var kim = new Person('kim', 10, 20, 30);
console.log('kim', kim);

// kim�̶�� ��ü���� �����ϰ� ���� �޼ҵ�
kim.sum = function () {
  return 'this : ' + (this.first + this.second);
};
var lee = new Person('lee', 10, 10, 10);
console.log('kim.sum()', kim.sum());
console.log('lee.sum()', lee.sum());
