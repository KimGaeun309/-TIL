var superObj = { superVal: 'super' };
// var subObj = { subVal: 'sub' };
// subObj.__proto__ = superObj; // �� __proto__ ����� ��ü�ϴ� �ڵ带 ¥����.
var subObj = Object.create(superObj); // �� �޼ҵ尡 superObj�� �θ�� �ϴ� ���ο� ��ü�� �����.
subObj.subVal = 'sub';
debugger;
console.log('subObj.subVal =>', subObj.subVal);
console.log('subObj.superVal =>', subObj.superVal);
subObj.superVal = 'sub'; // subObj��� ��ü�� ������Ƽ�� �ٲپ��� ��.
console.log('superObj.superVal =>', superObj.superVal);
console.log('subObj.superVal =>', subObj.superVal);

// ��ó�� Object.create()�� ����ؼ� ��ü�� ��ü ���� ��� ����, �� prototype link�� �������ִ� ���� �� ���� ����̴�.

// debugger; Ű���� �صΰ�
// html �����Ű��
// ������ ������ ���� reload�ϸ� source �ǿ� debugger; ���� ���� ����� Ȯ���� �� �ִ�.
// �̶� Watch�� ���� ��ü�� ���¸� �ڼ��� Ȯ���غ� �� �ִ�.

var kim = {
  name: 'kim',
  first: 10,
  second: 20,
  sum: function () {
    return this.first + this.second;
  },
};

// Object.create() ��� ���� ǥ��ȭ�� ǥ�� ���
var lee = Object.create(kim);
lee.name = 'lee';
lee.first = 10;
lee.second = 10;
lee.avg = function () {
  return (this.second + this.first) / 2;
};

// lee = {
//   name: 'lee',
//   first: 10,
//   second: 10,
//   avg: function () { // lee ���� ������ �Լ�
//     return (this.first + this.second) / 2;
//   },
// };
// lee.__proto__ = kim; // sum() �������� �ʾƵ� ��� ����
console.log('kim.sum() =>', kim.sum());
console.log('lee.sum() =>', lee.sum()); // lee ��ü�� sum()�� �ִ��� Ȯ��, �� ���� __proto__ �� sum()�� �ִ��� Ȯ��
console.log('lee.avg() =>', lee.avg());
