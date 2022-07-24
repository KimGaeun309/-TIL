# API와 CreateServer

## API

**A**pplication **P**rogramming **I**nterface

예를 들어, fs.readFile() 라는 함수는 누가 만들었을까? Node.js 를 만든 개발자들이 만들었다.

우리는 이 함수의 동작 원리는 모른다. Node.js 를 만든 개발자들은 Node.js 를 이용하는 개발자들에게 사용설명서를 통해 파일을 읽을 때에는 fs.readFile() 를 ~~한 방법으로 사용하라고 알려준다.

이런 약속된 조작 장치를 Interface라고 한다.

즉, 우리는 Interface를 실행시킴으로써 애플리케이션을 만들 수 있게 되는 것이다.

이처럼 application을 programming하기 위해 제공되는 interface를 API 라고 한다.

## Node.js의 API 문서

Node.js 홈페이지에서 해당 버전의 API 문서를 확인 가능하다.

HTTP 는 웹 브라우저와 웹 서버가 서로 통신할 때 사용하는 통신 규칙이고 그 통신을 지원하는 Node.js의 기능들이 HTTP 모듈에 있다.

HTTP 모듈 문서를 보면 createServer() 라고 하는 함수(메서드)가 있는데, 이 함수의 인자로는 requestListener 라는 parameter가 있는데, 대괄호가 쳐져 있으니 생략 가능하다.

설명을 보면 이 requestListener 는 함수이다. 따라서 우리는 main.js에서 createServer()의 인자로 매우 긴 함수를 넘겨준 것이다.

createServer()는 웹 서버를 만든다.

그리고 이 웹 서버로 외부에서 요청이 들어올 때마다 웹 서버는 이 createServer()인 인자인 함수를 호출하면서 이 함수의 첫번째 파라미터로는 웹브라우저로부터 들어온 요청에 대한 정보를 담고 있는 request 객체가 있고, 두번째 파라미터로는 이 함수 안의 구현을 통해 사용자에게 전송하고 싶은 정보(ex. `writeHead(200)`) 를 넘겨주기 위한 response 객체가 있다.

createServer()는 리턴 값으로 http.Server 를 반환한다. 그래서 var app 에는 이 객체가 담긴다.

app.listen(3000) 라는 코드도 있는데, 이때 listen()은 요청에 대해서 응답할 수 있도록 HTTP 서버를 구동시키는 API 이다.
