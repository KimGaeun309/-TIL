var superObj = { superVal: 'super' };
// var subObj = { subVal: 'sub' };
// subObj.__proto__ = superObj; // 이 __proto__ 사용을 대체하는 코드를 짜보자.
var subObj = Object.create(superObj); // 이 메소드가 superObj를 부모로 하는 새로운 객체를 만든다.
subObj.subVal = 'sub';
debugger;
console.log('subObj.subVal =>', subObj.subVal);
console.log('subObj.superVal =>', subObj.superVal);
subObj.superVal = 'sub'; // subObj라는 객체의 프로퍼티를 바꾸었을 뿐.
console.log('superObj.superVal =>', superObj.superVal);
console.log('subObj.superVal =>', subObj.superVal);

// 이처럼 Object.create()를 사용해서 객체와 객체 간의 상속 관계, 즉 prototype link를 지정해주는 것이 더 좋은 방법이다.

// debugger; 키워드 해두고
// html 실행시키고
// 개발자 도구에 가서 reload하면 source 탭에 debugger; 에서 멈춘 모습을 확인할 수 있다.
// 이때 Watch를 통해 객체의 상태를 자세히 확인해볼 수 있다.

var kim = {
  name: 'kim',
  first: 10,
  second: 20,
  sum: function () {
    return this.first + this.second;
  },
};

// Object.create() 라는 보다 표준화된 표현 사용
var lee = Object.create(kim);
lee.name = 'lee';
lee.first = 10;
lee.second = 10;
lee.avg = function () {
  return (this.second + this.first) / 2;
};

// lee = {
//   name: 'lee',
//   first: 10,
//   second: 10,
//   avg: function () { // lee 에만 정의한 함수
//     return (this.first + this.second) / 2;
//   },
// };
// lee.__proto__ = kim; // sum() 정의하지 않아도 사용 가능
console.log('kim.sum() =>', kim.sum());
console.log('lee.sum() =>', lee.sum()); // lee 객체에 sum()이 있는지 확인, 그 다음 __proto__ 에 sum()이 있는지 확인
console.log('lee.avg() =>', lee.avg());
