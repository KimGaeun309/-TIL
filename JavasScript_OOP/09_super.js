// ���� ����� ���ϴ� ����� �߰��ϰ� �ʹٸ�?
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

// ���� ���⿡ third ���� �߰��ϰ� �ʹٸ�?
class PersonPlus extends Person {
  constructor(name, first, second, third) {
    // ��ó�� �߰��� �� �ִ�. �׷��� �� ��� ����� ���ǰ� ������� �ȴ�.
    // this.name = name;
    // this.first = first;
    // this.second = second;

    // ���� �θ� ���� ����� super�� ����Ͽ� ������ �Ѵ�.
    super(name, first, second); // �θ� Ŭ������ Person�� �����ڰ� ȣ��ȴ�.
    this.third = third;
  }
  sum() {
    // return this.first + this.second + this.third;
    return super.sum() + this.third; // �θ� Ŭ������ Person�� sum() �� ȣ��ȴ�.
  }
  avg() {
    return (this.first + this.second + this.third) / 3;
  }
}

var kim = new PersonPlus('kim', 10, 20, 30);
console.log('kim.sum()', kim.sum());
console.log('kim.avg()', kim.avg());
