# App 제작 - 글 수정: 파일명 변경, 내용 저장

"/update_process" 에서 받은 정보를 토대로 파일을 수정하는 처리를 해보자.

POST 방식으로 넘겨진 정보를 읽어야 하므로 "/create_process" 에서 사용된 코드를 이용한다.

파일명을 변경할 때는 fs.rename()을 사용하고, 이 fs.rename() 의 callback 함수에서 fs.writeFile()을 사용해 description도 바꾸어준다.

```javascript
else if (pathname === '/update_process') {
    var body = '';
    request.on('data', function (data) {
      body = body + data;
    });
    request.on('end', function () {
      var post = qs.parse(body);
      var id = post.id;
      var title = post.title;
      var description = post.description;
      fs.rename(`./data/${id}`, `./data/${title}`, function (err) {
        fs.writeFile(`data/${title}`, description, 'utf8', function (err) {
          response.writeHead(302, { Location: `/?id=${title}` });
          response.end();
        });
      });
    });
  }
```
