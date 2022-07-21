# App 제작 - 파일을 이용해 본문 구현

query string에 따라 본문이 변경되는 웹 애플리케이션을 만들어보자.

```javascript
fs.readFile(`data/${queryData.id}.txt`, 'utf8', function (err, description) {
    var template = `
  <!doctype html>
<html>
<head>
  <title>WEB1 - ${title}</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="/">WEB</a></h1>
  <ol>
    <li><a href="/?id=HTML">HTML</a></li>
    <li><a href="?id=CSS">CSS</a></li>
    <li><a href="?id=JavaScript">JavaScript</a></li>
  </ol>
  <h2>${title}</h2>
  <p>
    ${description}
  </p>
</body>
</html>
  `;
    response.end(template);
  });
});
```

위와 같은 방법으로 본문을 구현한다.
이때 data 디렉토리 안에 있는 파일의 내용을 수정하면 main.js 의 실행을 멈췄다 다시 실행하지 않아도 새로고침하면 바로 반영된다.

클라이언트의 요청이 있을 때마다 파일 내용을 불러오기 때문이다.
