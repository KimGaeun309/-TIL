# APP 제작 - 파일 생성과 리다이렉션

1. 전송된 데이터를 data 디렉토라 안에 파일의 형태로 저장해보자. -> nodejs file write 검색

`fs.writeFile(fiel, data[, options], callback)` 을 사용해 file write를 할 수 있다.

```javascript
request.on('end', function () {
  var post = qs.parse(body);
  var title = post.title;
  var description = post.description;
  fs.writeFile(`./data/${title}`, description, 'utf8', function (err) {
    response.writeHead(200);
    response.end('success');
  });
});
```

2. redirection

`response.writeHead(301,{Location : URL})` -> 이 주소로 영원히 바꿈

`response.writeHead(302, {Location : URL})` -> 일시적으로 주소 바꿈
