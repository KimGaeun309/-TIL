// class 문법을 사용해 상속을 하는 것이 더 쉽고 분제도 덜 생기지만
// prototype을 통해 상속을 받는 방법을 알아보자. (class로 같은 기능 사용 가능)

// 1. call 을 사용해 생성자 함수가 생성자 함수를 상속하도록 만들어보자.

function Person(name, first, second) {
  this.name = name;
  this.first = first;
  this.second = second;
}

// Person이라고 하는 constructor function의 프로토타입으로 sum 을 만들기
// -> Person으로 만들어진 모든 객체들이 공유하는 메소드가 만들어짐
Person.prototype.sum = function () {
  return this.first + this.second;
};

function PersonPlus(name, first, second, third) {
  /* 같은 기능 중복
  this.name = name;
  this.first = first;
  this.second = second;
  */

  /* 이렇게 하면 안된다.
  Person(name, first, second); 
  여기에서의 this는 우리가 PersonPlus로 만든 객체가 아니기 때문.
  이 Person은 그냥 평범한 함수이다.
 */

  Person.call(this, name, first, second);
  // 이렇게 하면 call 메소드에 의해 이 코드가 실행되는데
  // 이 코드의 this는 우리가 생성하고자 하는 객체가 맞기 때문에 우리가 원하는 일을 한다.
  // 이 코드는 결국 super(name, first, second) 와 동일한 일을 한다.
  this.third = third;
}

/*
2. PersonPlus가 Person의 sum() 을 상속받으려면 어떻게 해야 할까?
생성자를 통해 상속하고 부모끼리 연결하는 벙법에 대해 알아보고 prototype과 __proto__의 차이에 데해 살펴보자.
kim 의 __proto__는 PersonPlus's prototype을 가리킨다. 여기에 현재 avg()는 있지만 sum()은 없다.
우리는 이 PersonPlus에서 sum()을 찾을 수 없을 때 Person의 prototype 객체에 있는 sum()을 호출하게 하고 싶다.
따라서 PersonPlus's prototype의 __proto__ 가 Person's prototype을 가리키도록 하면 된다.
*/

// PersonPlus.prototype.__proto__ = Person.prototype;  // 이 코드는 잘 동작하나 표준이 아니므로 아래 코드를 사용하는 것이 바람직하다.

PersonPlus.prototype = Object.create(Person.prototype); // Object.create()를 통해 Person.prototype을 __proto__ 로 하는 새로운 객체가 만들어진다.
// 하지만 이 경우 kim.constructor 가 Function: Person 이라고 나오게 된다. 하지만 kim의 constructor function은 PersonPlus여야 한다.
PersonPlus.prototype.constructor = PersonPlus; // 따라서 이 코드를 추가해야 한다.

// 3. constructor 프로퍼티를 이해해보자.
// kim.constructor는 이 kim 이라는 객체를 생성한 생성자이다.

PersonPlus.prototype.avg = function () {
  return (this.first + this.second + this.third) / 3;
};

var kim = new PersonPlus('kim', 10, 20, 30);

console.log('kim.sum()', kim.sum());
console.log('kim.avg()', kim.avg());
console.log('kim.constructor', kim.constructor);
