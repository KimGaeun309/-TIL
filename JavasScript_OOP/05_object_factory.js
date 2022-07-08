var kim = {
  name: 'kim',
  first: 10,
  second: 20,
  third: 30, // third 추가 (수정 작업)
  sum: function () {
    return this.first + this.second + this.third; // third 추가 (수정 작업)
  },
};
var lee = {
  name: 'lee',
  first: 10,
  second: 10,
  third: 10, // third 추가 (수정 작업)
  sum: function () {
    return this.first + this.second + this.third; // third 추가 (수정 작업)
  },
};
// 객체의 개수가 많다면? 수정이 어려워짐. -> 객체를 찍어내는 공장을 만들어 객체를 양산하자.
console.log('kim.sum()', kim.sum());
console.log('lee.sum()', lee.sum());

// 새로운 객체가 만들어져 d1이 된다 -> 이 객체의 설계도가 우리 눈에 보이지 않지만 이 객체를 쓸 수 있다.
var d1 = new Date('2019-4-10');
console.log('d1.getFullYear()', d1.getFullYear());
console.log('d1.getMonth()', d1.getMonth());

console.log('Date', Date);

function Person() {
  (this.name = 'kim'),
    (this.first = 10),
    (this.second = 20),
    (this.third = 30), // third 추가 (수정 작업)
    (this.sum = function () {
      return this.first + this.second; // this 사용헤 자신이 속한 객체를 가리킴
    });
}
console.log('Person()', Person());
// constructor (생성자)
console.log('new Person()', new Person());

console.log('---------------------------------------------');
function Person(name, first, second, third) {
  (this.name = name),
    (this.first = first),
    (this.second = second),
    (this.third = third), // third 추가 (수정 작업)
    (this.sum = function () {
      return this.first + this.second + this.third; // this 사용헤 자신이 속한 객체를 가리킴
    });
}
var kim = new Person('kim', 10, 20, 30);
var lee = new Person('lee', 10, 10, 10);

console.log('kim.sum()', kim.sum());
console.log('lee.sum()', lee.sum());

// constructor 로 만들 경우, new를 사용함으로써 실행할 때마다 객체가 양산된다.
// 그리고 construct function의 내용을 수정하면 그를 사용하는 다른 모든 갹채들의 내용이 한번에 수정된다.
