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
  //console.log(__dirname + url); // �� �ڵ带 �����غ���
  //����ڰ� ������ ������ javascript�� ���ؼ� �츮�� �о�鿩�� �� ������ ����� �ȴٴ� �� �� �� �ִ�.
  response.end(fs.readFileSync(__dirname + url));
});
app.listen(3000);
