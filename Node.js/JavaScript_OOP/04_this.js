var kim = {
  name: 'kim',
  first: 10,
  second: 20,
  sum: function () {
    return this.first + this.second; // this 사용헤 자신이 속한 객체를 가리킴
  },
};
// console.log('kim.sum(kim.first, kim.second)', kim.sum(kim.first, kim.second));
console.log('kim.sum()', kim.sum());
