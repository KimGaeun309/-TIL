// js를 만든 사람들은 Math라는 이름의 객체를 만들어 PI random, floor 와 같은 수학과 관련된 변수와 함수들을 잘 정리함.
console.log('Math.PI', Math.PI);
console.log('Math.random()', Math.random());
console.log('Math.floor(3.9)', Math.floor(3.9));

// 객체 만들기
var MyMath = {
  PI: Math.PI,
  random: function () {
    return Math.random();
  },
  floor: function (val) {
    return Math.floor(val);
  },
};

console.log('MyMath.PI', MyMath.PI);
console.log('MyMath.random()', MyMath.random());
console.log('MyMath.floor(3.9)', MyMath.floor(3.9));

// 객체는 같은 취지의 서로 연관된 변수와 함수들을 객체로 그룹핑해 이름을 붙여 활용하는 것이다.

// 이런 식으로 이름 충돌을 방지할 수도 있지만 덜 세련되었다.
var MyMath_PI = Math.PI;
function MyMath_random() {
  return Math.random();
}
function MyMath_floor(val) {
  return Math.floor(val);
}
