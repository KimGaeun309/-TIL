// 이 Person()은 함수이지만 이를 사용할 때 앞에 new를 붙이면 객체가 return된다.
// new를 붙이면 Person()은 constructor가 된다.
// constructor는 객체를 만들고 그 객체의 초기 상태를 설정하는 역할을 한다.
function Person(name, first, second, third) {
  this.name = name;
  this.first = first;
  this.second = second;
  this.third = third; // third 추가 (수정 작업)
  // this.sum = function () {
  //   return this.first + this.second + this.third; // this 사용헤 자신이 속한 객체를 가리킴
  // };
}

// prototype -> 여러 개의 객체가 한 가지 함수를 공유
Person.prototype.sum = function () {
  return 'prototype : ' + (this.first + this.second + this.third);
};

var kim = new Person('kim', 10, 20, 30);
kim.sum = function () {
  // kim의 sum()만 수정
  return 'this : ' + (this.first + this.second);
};
// kim.sum = function () { // 모든 객체의 sum 함수를 이렇게 바꾸려면 하나하나 수정해야 함
//   return 'modified : ' + (this.first + this.second + this.third);
// };
var lee = new Person('lee', 10, 10, 10);
// lee.sum = function () { // 모든 객체의 sum 함수를 이렇게 바꾸려면 하나하나 수정해야 함
//   return 'modified : ' + (this.first + this.second + this.third);
// };
console.log('kim.sum()', kim.sum());
console.log('lee.sum()', lee.sum());

// -> prototype 사용해 해결
