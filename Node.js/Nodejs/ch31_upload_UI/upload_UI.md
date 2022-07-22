# 글생성 UI 만들기

## 웹사이트의 글목록 리스트 아래에 create 페이지를 생성

- templateHTML() 에서 list 와 body 사이에 create 링크를 생성한다.

```javascript
function templateHTML(title, list, body) {
  return `
  <!doctype html>
  <html>
    <head>
      <title>WEB1 - ${title}</title>
      <meta charset="utf-8">
    </head>
    <body>
      <h1><a href="/">WEB1</a></h1>
      ${list}
      <a href="/create">create</a>
      ${body}
    </body>
    </html>
  `;
}
```

- '/create' 링크를 처리하기 위해 조건문을 추가한다. (home page 생성할 때 사용한 코드 참고해 작성)

```javascript
else if (pathname === '/create') {
    fs.readdir('ch26_use_function/data', function (error, filelist) {
      var title = 'WEB - create';
      var list = templateList(filelist);
      var template = templateHTML(
        title,
        list,
        `
        <form action="http://localhost:3000/process create" method="post">
          <p>
            <input type="text" name="title" placeholder="title" />
          </p>

          <p>
            <textarea name="description" placeholder="description"></textarea>
          </p>

          <p>
            <input type="submit" />
          </p>
        </form>

        `
      );
      response.writeHead(200);
      response.end(template);
    });
```

이후 create 에 생성된 title과 description에 정보를 적고 submit 버튼을 클릭하면 개발자 도구 - network - process%20create - Payload 에 Form 형태로 작성된 정보를 확인할 수 있다.
