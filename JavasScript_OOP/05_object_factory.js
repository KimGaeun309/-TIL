var kim = {
  name: 'kim',
  first: 10,
  second: 20,
  third: 30, // third �߰� (���� �۾�)
  sum: function () {
    return this.first + this.second + this.third; // third �߰� (���� �۾�)
  },
};
var lee = {
  name: 'lee',
  first: 10,
  second: 10,
  third: 10, // third �߰� (���� �۾�)
  sum: function () {
    return this.first + this.second + this.third; // third �߰� (���� �۾�)
  },
};
// ��ü�� ������ ���ٸ�? ������ �������. -> ��ü�� ���� ������ ����� ��ü�� �������.
console.log('kim.sum()', kim.sum());
console.log('lee.sum()', lee.sum());

// ���ο� ��ü�� ������� d1�� �ȴ� -> �� ��ü�� ���赵�� �츮 ���� ������ ������ �� ��ü�� �� �� �ִ�.
var d1 = new Date('2019-4-10');
console.log('d1.getFullYear()', d1.getFullYear());
console.log('d1.getMonth()', d1.getMonth());

console.log('Date', Date);

function Person() {
  (this.name = 'kim'),
    (this.first = 10),
    (this.second = 20),
    (this.third = 30), // third �߰� (���� �۾�)
    (this.sum = function () {
      return this.first + this.second; // this ����� �ڽ��� ���� ��ü�� ����Ŵ
    });
}
console.log('Person()', Person());
// constructor (������)
console.log('new Person()', new Person());

console.log('---------------------------------------------');
function Person(name, first, second, third) {
  (this.name = name),
    (this.first = first),
    (this.second = second),
    (this.third = third), // third �߰� (���� �۾�)
    (this.sum = function () {
      return this.first + this.second + this.third; // this ����� �ڽ��� ���� ��ü�� ����Ŵ
    });
}
var kim = new Person('kim', 10, 20, 30);
var lee = new Person('lee', 10, 10, 10);

console.log('kim.sum()', kim.sum());
console.log('lee.sum()', lee.sum());

// constructor �� ���� ���, new�� ��������ν� ������ ������ ��ü�� ���ȴ�.
// �׸��� construct function�� ������ �����ϸ� �׸� ����ϴ� �ٸ� ��� ��ä���� ������ �ѹ��� �����ȴ�.
