var kim = { name: 'kim', first: 10, second: 20 };
var lee = { name: 'lee', first: 10, second: 10 };

function sum(prefix) {
  return prefix + (this.first + this.second);
}

// sum.call(); �� sum(); �� ����.
console.log('sum.call(kim)', sum.call(kim, '=> ')); // sum�̶�� ��ü�� �����Ű�� ��.
// js������ �Լ��� ��ü�̴�.
// call�ƶ�� �Լ��� method�� ������ �� kim�̶�� ��ü�� ���ڷ� �ָ� �� sum()�� ������ �� this = kim �� �ȴ�.
console.log('sum.call(lee)', sum.call(lee, ': ')); // lee�� ���ڷ� �ָ� sum()���� this �� lee �� �ȴ�.
// �� call�̶�� �Լ��� ù��° ���ڷ� this�� ���� ��ü�� ������ ������, �� ���� ���ں��ʹ� sum()�� �������� ���� ���� ���´�.

// bind : sum�� ȣ��� ������ this�� ���ϴ� �� �ƴ϶� ���������� ����� this�� �����ϰ� ���� �� ���
var kimSum = sum.bind(kim, '-> '); // -> this�� kim���� �ϴ� ���ο� �Լ��� �����ȴ�. ���������� ���� ���ڸ� ������ �� �ִ�.
console.log('kimSum()', kimSum());
// sum()�� �ٲ��� ����. ������ �°� �ٲ� ���ο� �Լ��� return�Ǿ� kimSum�� ���Ե�.
// ��, bind�� this�� ���� ���������� �ٲٴ� ���ο� �Լ��� �����.
