/*

�Լ��� ���� �߰�ȣ�� ������. 
�Լ��� javascript���� statementó�� �������� ��� ��ü�̴�.
�׷��� �Լ��� 
function() Peron() {} 
var Person = new Function();
�� �� ��� ������ε� �ڹٽ�ũ��Ʈ�� �Լ��� ���� �� �ִ�.

function Person(name, first, second) {
  this.name = name;
  this.first = first;
  this.second = second;
}
-> Person�̶�� ��ü�� Person�� prototype�̶�� ��ü�� �����. (�� �� ���� ��ü�� ����)
�̶� Person�̶�� ��ü�� prototype�̶�� ������Ƽ�� ����� �̰��� Person's prototype�� ����Ű�� �ȴ�.
Person's prototype�̶�� ��ü�� constructor��� ������Ƽ�� ����� �̰��� Person�� ����Ű�� �ȴ�.
�� ���� ���� ��ȣ������ �ϴ� ���̴�.

Person.prototype.sum = function() {}
�� �ڵ带 �����ϸ� Person's prototype�� sum �Լ��� �����.

var kim = new Person('kim', 10, 20)
�� �ڵ带 �äӤ����ϸ� kim�̶�� ��ü�� �����ȴ�. __proto__ �� name, first, second ������Ƽ�� �����.
�� __proto__ ������Ƽ�� �� kim�̶�� ��ü�� ������ Person�� prototype �� ����Ų��. 

console.log(kim.sum())
kim ��ü���� sum()�� �����Ƿ� __proto__ �� ����Ű�� Person's prototype�� sum()�� �ִ��� Ȯ���Ѵ�.

Person�� prototype �̶�� ������Ƽ��
kim�� __proto__ ��� ������Ƽ�� ��� �ٸ���?
-> __proto__ ��� ������Ƽ�� �ʱ⿡�� ������ ��ü�� ����Ű���� �������� ���� ����.
-> prototype ������Ƽ�� �Լ��� �����ɶ� ��������� ������Ÿ�Ը��� ����Ű�� ���� �Ұ���

*/
