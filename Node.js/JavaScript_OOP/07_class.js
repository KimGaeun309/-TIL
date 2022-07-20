/* javascript는 가장 빠르게 발전하는 언어 중 하나.
  class는 java, python 등 여러 언어들이 객체를 만드는 동작으로 지원했는데
  javascript는 그런 지원을 하지 않았었지만 class를 도입해서 이미 다른 컴퓨터 언어에서 사용하던 객체 지향을
  구사하기 쉬워짐. */

/* class는 객체를 찍어내는 공장, construct function의 대체재라고 할 수 있다.
  class는 ECMA script 6부터 도입된 문법이다.
  오늘날 많은 웹프라우저와 Node.js 와 같은 플랫폼들이 ECMA script 6 이상의 버전 지원한다.
  javascript는 원래 객체 지향 언어이므로 새롭게 도입된 문법은 이미 존재하던 기능ㅇ르 변형한 것으로, 
  기존의 문법으로도 나타낼 수 있다. */

// prototype.js 와 똑같이 동작하는 것을 class로 만들어보자.

class Person {
  //sum() {} // -> function 이라는 키워드 없이 함수 정의
  constructor(name, first, second, third) {
    // 객체가 생성될 때 실행되는 함수!
    // constructor 함수로 초기값 세팅 가능.
    console.log('constructor');
    this.name = name;
    this.first = first;
    this.second = second;
    this.third = third;
  }
  // class에 메소드 추가 방법2: 내부에 정의
  sum() {
    // 이 메소드는 모든 객체에 적용됨
    return 'prototype : ' + (this.first + this.second + this.third);
  }
}

// class에 메소드 추가 방법 1: prototype 그대로 사용
// Person.prototype.sum = function () {
//   return 'prototype : ' + (this.first + this.second + this.third);
// };

// 객체를 생성하고 초기값 설정
var kim = new Person('kim', 10, 20, 30);
console.log('kim', kim);

// kim이라는 객체에만 적용하고 싶은 메소드
kim.sum = function () {
  return 'this : ' + (this.first + this.second);
};
var lee = new Person('lee', 10, 10, 10);
console.log('kim.sum()', kim.sum());
console.log('lee.sum()', lee.sum());
