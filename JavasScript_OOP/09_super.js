// 만약 평균을 구하는 기능을 추가하고 싶다면?
class Person {
  constructor(name, first, second) {
    this.name = name;
    this.first = first;
    this.second = second;
  }
  sum() {
    return this.first + this.second;
  }
}

// 만약 여기에 third 인자 추가하고 싶다면?
class PersonPlus extends Person {
  constructor(name, first, second, third) {
    // 이처럼 추가할 수 있다. 그러나 이 경우 상속의 의의가 사라지게 된다.
    // this.name = name;
    // this.first = first;
    // this.second = second;

    // 따라서 부모가 가진 기능은 super를 사용하여 만들어야 한다.
    super(name, first, second); // 부모 클래스인 Person의 생성자가 호출된다.
    this.third = third;
  }
  sum() {
    // return this.first + this.second + this.third;
    return super.sum() + this.third; // 부모 클래스인 Person의 sum() 이 호출된다.
  }
  avg() {
    return (this.first + this.second + this.third) / 3;
  }
}

var kim = new PersonPlus('kim', 10, 20, 30);
console.log('kim.sum()', kim.sum());
console.log('kim.avg()', kim.avg());
