// class ������ ����� ����� �ϴ� ���� �� ���� ������ �� ��������
// prototype�� ���� ����� �޴� ����� �˾ƺ���. (class�� ���� ��� ��� ����)

// 1. call �� ����� ������ �Լ��� ������ �Լ��� ����ϵ��� ������.

function Person(name, first, second) {
  this.name = name;
  this.first = first;
  this.second = second;
}

// Person�̶�� �ϴ� constructor function�� ������Ÿ������ sum �� �����
// -> Person���� ������� ��� ��ü���� �����ϴ� �޼ҵ尡 �������
Person.prototype.sum = function () {
  return this.first + this.second;
};

function PersonPlus(name, first, second, third) {
  /* ���� ��� �ߺ�
  this.name = name;
  this.first = first;
  this.second = second;
  */

  /* �̷��� �ϸ� �ȵȴ�.
  Person(name, first, second); 
  ���⿡���� this�� �츮�� PersonPlus�� ���� ��ü�� �ƴϱ� ����.
  �� Person�� �׳� ����� �Լ��̴�.
 */

  Person.call(this, name, first, second);
  // �̷��� �ϸ� call �޼ҵ忡 ���� �� �ڵ尡 ����Ǵµ�
  // �� �ڵ��� this�� �츮�� �����ϰ��� �ϴ� ��ü�� �±� ������ �츮�� ���ϴ� ���� �Ѵ�.
  // �� �ڵ�� �ᱹ super(name, first, second) �� ������ ���� �Ѵ�.
  this.third = third;
}

/*
2. PersonPlus�� Person�� sum() �� ��ӹ������� ��� �ؾ� �ұ�?
�����ڸ� ���� ����ϰ� �θ𳢸� �����ϴ� ������ ���� �˾ƺ��� prototype�� __proto__�� ���̿� ���� ���캸��.
kim �� __proto__�� PersonPlus's prototype�� ����Ų��. ���⿡ ���� avg()�� ������ sum()�� ����.
�츮�� �� PersonPlus���� sum()�� ã�� �� ���� �� Person�� prototype ��ü�� �ִ� sum()�� ȣ���ϰ� �ϰ� �ʹ�.
���� PersonPlus's prototype�� __proto__ �� Person's prototype�� ����Ű���� �ϸ� �ȴ�.
*/

// PersonPlus.prototype.__proto__ = Person.prototype;  // �� �ڵ�� �� �����ϳ� ǥ���� �ƴϹǷ� �Ʒ� �ڵ带 ����ϴ� ���� �ٶ����ϴ�.

PersonPlus.prototype = Object.create(Person.prototype); // Object.create()�� ���� Person.prototype�� __proto__ �� �ϴ� ���ο� ��ü�� ���������.
// ������ �� ��� kim.constructor �� Function: Person �̶�� ������ �ȴ�. ������ kim�� constructor function�� PersonPlus���� �Ѵ�.
PersonPlus.prototype.constructor = PersonPlus; // ���� �� �ڵ带 �߰��ؾ� �Ѵ�.

// 3. constructor ������Ƽ�� �����غ���.
// kim.constructor�� �� kim �̶�� ��ü�� ������ �������̴�.

PersonPlus.prototype.avg = function () {
  return (this.first + this.second + this.third) / 3;
};

var kim = new PersonPlus('kim', 10, 20, 30);

console.log('kim.sum()', kim.sum());
console.log('kim.avg()', kim.avg());
console.log('kim.constructor', kim.constructor);
