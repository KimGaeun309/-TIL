# URL을 통해서 입력된 값 사용하기

`http://localhost/?id=HTML`

`id=HTML` 부분을 query string이라 하는데, 이에 따라 다른 정보를 보여주는 것을 해보자.

## main.js

- 현재 URL은 `localhost:3000/3.html` 이다.
- 이를 `localhost:3000/?id=JavaScript` 를 받으면 3.html 페이지를 보여주도록 수정해보자.
- `id=JavaScript` 는 request.url 에 반영된다.
- 즉 이로부터 데이터를 추출할 수 있어야 한다.
- nodejs url parse query string 검색

`var url = require('url');` -> url 이라는 모듈 사용

`var queryData = url.parse(_url, true).query;` -> query string을 객체로 받아 사용
