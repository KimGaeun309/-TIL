/* 
�ٸ� �ַ� ��ü ���� ������ Ŭ������ ����� �޴µ�,
javascript������ ��ü�� ���� �ٸ� ��ü�� ����� ���� �� �ְ�
�󸶵��� ��� ���踦 �ٲ� �� �ִ�. 
(prototype link �� �ٲپ��ָ� �ȴ�. �̶� prototype link�� ����Ű�� ��ü�� prototype object��� �Ѵ�.) */

var superObj = { superVal: 'super' };
var subObj = { subVal: 'sub' };
// �� �� ������Ʈ�� ���� �����̴�. ������ javascript������ �̸� ��� ����� �ٲ� �� �ִ�.

subObj.__proto__ = superObj; // �̷��� �ϸ� ��� ���谡 �����ȴ�.
console.log('subObj.subVal =>', subObj.subVal);
console.log('subObj.superVal =>', subObj.superVal);
subObj.superVal = 'sub'; // subObj��� ��ü�� ������Ƽ�� �ٲپ��� ��.
console.log('superObj.superVal =>', superObj.superVal);
console.log('subObj.superVal =>', subObj.superVal);

// prototype, __proto__ �� �ִµ�, �� �� ȥ�������� �� �ִ�.
// prototype�� ���ϸ� constructor �ۿ��� method�� ������ �� �ִ�.
// __proto__ �� ��ü �� ����� ������ �Ѵ�.
