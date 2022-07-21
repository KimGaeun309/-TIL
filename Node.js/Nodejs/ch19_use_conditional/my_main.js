// var template 이 중복된다고 느껴 수정해보았다.

var http = require('http');
var fs = require('fs');
var url = require('url'); // url 이라는 모듈 사용

var app = http.createServer(function (request, response) {
  var _url = request.url;
  var queryData = url.parse(_url, true).query;

  var pathname = url.parse(_url, true).pathname;

  if (pathname === '/') {
    // 올바른 경로로 접속함

    fs.readFile(`data/${queryData.id}`, 'utf8', function (err, description) {
      var title = queryData.id;

      if (title == undefined) {
        title = 'Welcome';
        description = 'Hello, Node.js';
      }

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
      response.writeHead(200); // 200 을 서버가 브라우저에게 주면 파일을 성공적으로 전송했다는 뜻.
      response.end(template);
    });
  } else {
    // 잘못된 경로로 접속함 ->  오류 메시지
    response.writeHead(404); // 404 를 주면 파일을 찾을 수 없는 경우라는 뜻.
    response.end('Not found');
  }
});
app.listen(3000);
