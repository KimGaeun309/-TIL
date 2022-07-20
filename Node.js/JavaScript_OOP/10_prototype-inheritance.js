/* 
다른 주류 객체 지향 언어에서는 클래스가 상속을 받는데,
javascript에서는 객체가 직접 다른 객체의 상속을 받을 수 있고
얼마든지 상속 관계를 바꿀 수 있다. 
(prototype link 만 바꾸어주면 된다. 이때 prototype link가 가리키는 객체를 prototype object라고도 한다.) */

var superObj = { superVal: 'super' };
var subObj = { subVal: 'sub' };
// 이 두 오브젝트는 서로 남남이다. 하지만 javascript에서는 이를 상속 관계로 바꿀 수 있다.

subObj.__proto__ = superObj; // 이렇게 하면 상속 관계가 성립된다.
console.log('subObj.subVal =>', subObj.subVal);
console.log('subObj.superVal =>', subObj.superVal);
subObj.superVal = 'sub'; // subObj라는 객체의 프로퍼티를 바꾸었을 뿐.
console.log('superObj.superVal =>', superObj.superVal);
console.log('subObj.superVal =>', subObj.superVal);

// prototype, __proto__ 가 있는데, 이 용어가 혼란스러울 수 있다.
// prototype을 통하면 constructor 밖에서 method를 지정할 수 있다.
// __proto__ 는 객체 간 상속을 가능케 한다.
