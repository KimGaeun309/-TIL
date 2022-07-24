# App 제작 - 입력정보에 대한 보안

## 수업의 최종적인 목적

- 보안 문제가 왜 생기는지,
- 보안 문제를 어떤 식으로 해결할 수 있는지,
- 보안이 왜 중요한지

에 대해 살펴보기

## 보안 위험 요소 1. 오염된 정보가 들어오는 것

- 예를 들어, 우리 애필리케이션 안에 database를 통해 데이터를 관리하게 될 텐데, database는 id 와 password만 있어야 데이터를 가져올 수 있어서 그 정보를 어딘가에 저장해야 하는데, password.js 파일에 이를 저장한다고 생각해보자.

  - 이 파일은 http://localhost:3000/?id=../password.js 를 URL로 쓰면 그 내용이 웹 페이지에 출력되어 버린다.
  - 또 이런 식으로 상위 디렉토리로 가면서 탐색할 수 있어 위함하다.

- 이 문제를 해결하기 위해 path.parse().base 를 이용해보자.

```javascript
> var path = require('path');
undefined
> path.parse('password.js');
{
  root: '',
  dir: '',
  base: 'password.js',
  ext: '.js',
  name: 'password'
}
> path.parse('../password.js').base;
'password.js'
```

path.parse(URL).base를 하면 URL에서 ../ 가 삭제된다.

readFile()을 하는 곳을 다음과 같이 바꾸자.

```javascript
fs.readdir('./data', function (error, filelist) {
  var filteredID = path.parse(queryData.id).base; // 추가한 코드
  fs.readFile(
    `./data/${filteredId}`, // 바뀐 코드
    'utf8',
    function (err, description) {
      var title = queryData.id;
      var list = template.list(filelist);
      var html = template.HTML(
        title,
        list,
        `<h2>${title}</h2>${description}`,
        `<a href="/create">create</a>
              <a href="/update?id=${title}">update</a>
              <form action="delete_process" method="post">
              <input type="hidden" name="id" value="${title}">
              <input type="submit" value="delete">
              </form>`
      );
      response.writeHead(200);
      response.end(html);
    }
  );
});
```

또, password.js 의 내용을 삭제할 수도 있으므로 delete 부분도 다음과 같이 바꾸자.

```javascript
request.on('end', function () {
  var post = qs.parse(body);
  var id = post.id;
  var filteredId = path.parse(id).base;
  fs.unlink(`data/${filteredId}`, function (err) {
    response.writeHead(302, { Location: `/` });
    response.end();
  });
});
```
