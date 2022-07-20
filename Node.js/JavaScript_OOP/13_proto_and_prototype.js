/*

함수는 끝에 중괄호로 끈난다. 
함수는 javascript에서 statement처럼 보이지만 사실 객체이다.
그래서 함수는 
function() Peron() {} 
var Person = new Function();
둘 중 어느 방법으로든 자바스크립트의 함수를 만들 수 있다.

function Person(name, first, second) {
  this.name = name;
  this.first = first;
  this.second = second;
}
-> Person이라는 객체와 Person의 prototype이라는 객체가 생긴다. (총 두 개의 객체가 생김)
이때 Person이라는 객체에 prototype이라는 프로퍼티가 생기고 이것은 Person's prototype을 가리키게 된다.
Person's prototype이라는 객체도 constructor라는 프로퍼티가 생기고 이것은 Person을 가리키게 된다.
즉 서로 간에 상호참조를 하는 것이다.

Person.prototype.sum = function() {}
이 코드를 실행하면 Person's prototype에 sum 함수가 생긴다.

var kim = new Person('kim', 10, 20)
이 코드를 시ㅣㄹ행하면 kim이라는 객체가 생성된다. __proto__ 와 name, first, second 프로퍼티가 생긴다.
이 __proto__ 프로퍼티는 이 kim이라는 객체를 생성한 Person의 prototype 을 가리킨다. 

console.log(kim.sum())
kim 객체에는 sum()이 없으므로 __proto__ 가 가리키는 Person's prototype에 sum()이 있는지 확인한다.

Person의 prototype 이라는 프로퍼티와
kim의 __proto__ 라는 프로퍼티가 어떻게 다른가?
-> __proto__ 라는 프로퍼티는 초기에는 생성자 객체를 가리키지만 참조관계 변경 가능.
-> prototype 프로퍼티는 함수가 생성될때 만들어지는 프로토타입만을 가리키며 변경 불가능

*/
