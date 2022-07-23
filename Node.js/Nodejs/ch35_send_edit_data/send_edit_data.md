# App 제작 - 글 수정: 수정할 정보 전송

/update 페이지에 대한 처리를 해주는 else if 문을 추가하자.

- 이때 앞에서 파일 읽기를 할 때 쓴 코드와, create의 form 코드를 사용한다.
- 단, input의 경우 value로 원래 데이터를 보여주고, textarea의 경우 태그 사이에 데이터를 보여주어야 한다.
- 또, 사용자가 제목을 수정할 때 원래 제목을 알아야 data 디렉토리에서 해당 파일을 수정할 수 있으므로 hidden 타입의 태그에 원래 제목을 넣어준다.

```javascript
else if (pathname === '/update') {
    fs.readdir('./data', function (error, filelist) {
      fs.readFile(
        `./data/${queryData.id}`,
        'utf8',
        function (err, description) {
          var title = queryData.id;
          var list = templateList(filelist);
          var template = templateHTML(
            title,
            list,
            `
            <form action="/update_process" method="post">
            <input type="hidden" name="id" value="${title}">
            <p>
              <input type="text" name="title" placeholder="title" value=${title}/>
            </p>

            <p>
              <textarea name="description" placeholder="description">${description}</textarea>
            </p>

            <p>
              <input type="submit" />
            </p>
          </form>

            `,
            `<a href="/create">create</a> <a href="/update?id=${title}">update</a>`
          );
          response.writeHead(200);
          response.end(template);
        }
      );
    });
  }
```
