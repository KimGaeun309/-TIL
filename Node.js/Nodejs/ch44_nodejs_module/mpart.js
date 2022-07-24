var M = {
  v: 'v',
  f: function () {
    console.log(this.v);
  },
};

module.exports = M; // 우리가 지금 만들고 있는 모듈이 담긴 mpart.js 라는 파일에 있는 여러 기능들 중
// M 이 가리키는 객체를 이 모듈 바깥에서 사용할 수 있도록 exports 하겠다
