# App 제작 - 글 삭제: 삭제 기능 완성

"/update_process" 의 코드를 참조한다.

`fs.unlink(path, callback)` 을 사용해 삭제한다.

```javascript
else if (pathname === '/delete_process') {
    var body = '';
    request.on('data', function (data) {
      body = body + data;
    });
    request.on('end', function () {
      var post = qs.parse(body);
      var id = post.id;
      fs.unlink(`data/${id}`, function (err) {
        response.writeHead(302, { Location: `/` });
        response.end();
      });
    });
  }
```
