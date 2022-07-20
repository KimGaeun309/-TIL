// ���� ����� ���ϴ� ����� �߰��ϰ� �ʹٸ�?
class Person {
  constructor(name, first, second) {
    this.name = name;
    this.first = first;
    this.second = second;
  }
  sum() {
    return 'prototype : ' + (this.first + this.second);
  }

  /* ��� 1. ��ó�� class �ȿ� ���ο� �޼ҵ带 �߰��ص� �ȴ�.
  avg() {
  return (this.first + this.second) / 2;
  }

  ������ ���̺귯���� ����ϴ� ���, Ȥ�� avg()�� �׻� ��������� �ʴ� ��� ���� �ڵ尡 �ƴϴ�.
  */
}

/* ��� 2. Ŭ������ �ϳ� �� ���� �ȴ�.
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
// ������ �� ��� �ڵ��� �ߺ��� ��������.

// ��� 3. ���(inheritance) �� ����Ѵ�.
class PersonPlus extends Person {
  avg() {
    return (this.first + this.second) / 2;
  }
}

var kim = new PersonPlus('kim', 10, 20);
console.log('kim.sum()', kim.sum());
console.log('kim.avg()', kim.avg());

// ����� ����ϸ� �ߺ��Ǵ� �ڵ带 �����Ͽ� �ڵ��� ���� �ٿ���,
// Ŭ������ �ڵ带 ������ �� �� Ŭ������ ����ϴ� ��� Ŭ������ ���ôٹ������� ������ �Ͼ ���� ������ ��������.
