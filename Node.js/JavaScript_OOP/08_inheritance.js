// 만약 평균을 구하는 기능을 추가하고 싶다면?
class Person {
  constructor(name, first, second) {
    this.name = name;
    this.first = first;
    this.second = second;
  }
  sum() {
    return 'prototype : ' + (this.first + this.second);
  }

  /* 방법 1. 이처럼 class 안에 새로운 메소드를 추가해도 된다.
  avg() {
  return (this.first + this.second) / 2;
  }

  하지만 라이브러리를 사용하는 경우, 혹은 avg()를 항상 사용하지는 않는 경우 좋은 코드가 아니다.
  */
}

/* 방법 2. 클래스를 하나 더 만들어도 된다.
class PersonPlus {
  constructor(name, first, second) {
    this.name = name;
    this.first = first;
    this.second = second;
  }
  sum() {
    return 'prototype : ' + (this.first + this.second);
  }
  avg() {
    return (this.first + this.second) / 2;
  }
}
*/
// 하지만 이 경우 코드의 중복이 많아진다.

// 방법 3. 상속(inheritance) 을 사용한다.
class PersonPlus extends Person {
  avg() {
    return (this.first + this.second) / 2;
  }
}

var kim = new PersonPlus('kim', 10, 20);
console.log('kim.sum()', kim.sum());
console.log('kim.avg()', kim.avg());

// 상속을 사용하면 중복되는 코드를 제거하여 코드의 양을 줄였고,
// 클래스의 코드를 수정할 때 그 클래스를 상속하는 모든 클래스에 동시다발적으로 변경이 일어나 유지 보수가 편리해진다.
