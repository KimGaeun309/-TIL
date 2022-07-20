var http = require('http');
var fs = require('fs');
var app = http.createServer(function (request, response) {
  var url = request.url;
  if (request.url == '/') {
    url = '/index.html';
  }
  if (request.url == '/favicon.ico') {
    //return response.writeHead(404);
    response.writeHead(404);
    response.end();
    return;
  }
  response.writeHead(200);
  //console.log(__dirname + url); // 이 코드를 실행해보면
  //사용자가 접근할 때마다 javascript를 통해서 우리가 읽어들여야 할 파일을 만들게 된다는 걸 알 수 있다.
  response.end(fs.readFileSync(__dirname + url));
});
app.listen(3000);
