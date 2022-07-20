var kim = { name: 'kim', first: 10, second: 20 };
var lee = { name: 'lee', first: 10, second: 10 };

function sum(prefix) {
  return prefix + (this.first + this.second);
}

// sum.call(); 은 sum(); 과 동일.
console.log('sum.call(kim)', sum.call(kim, '=> ')); // sum이라는 객체를 실행시키는 것.
// js에서는 함수도 객체이다.
// call아라는 함수의 method를 실행할 때 kim이라는 객체를 인자로 주면 이 sum()을 실행할 때 this = kim 이 된다.
console.log('sum.call(lee)', sum.call(lee, ': ')); // lee를 인자로 주면 sum()에서 this 는 lee 가 된다.
// 이 call이라는 함수는 첫번째 인자로 this로 무슨 객체를 쓸지가 들어오고, 그 다음 인자부터는 sum()에 저낟ㄹ될 인자 값이 들어온다.

// bind : sum이 호출될 때마다 this를 정하는 게 아니라 내부적으로 사용할 this를 고정하고 싶을 때 사용
var kimSum = sum.bind(kim, '-> '); // -> this를 kim으로 하는 새로운 함수가 생성된다. 마찬가지고 사용될 인자를 지정할 수 있다.
console.log('kimSum()', kimSum());
// sum()은 바뀌지 않음. 취지에 맞게 바뀐 새로운 함수가 return되어 kimSum에 대입됨.
// 즉, bind는 this의 값을 영구적으로 바꾸는 새로운 함수를 만든다.
