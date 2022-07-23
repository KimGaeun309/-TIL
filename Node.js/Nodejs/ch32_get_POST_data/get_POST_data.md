# APP 제작 - POST 방식으로 전송된 데이터 받기

## create_process 로 생성된 페이지에서 정보를 받을 수 있어야 한다.

1. create 창의 form 에서 입력한 정보를 "/create_process" 에서 받을 수 있도록 코드를 수정한다.

```javascript
else if (pathname === '/create') {
    fs.readdir('ch26_use_function/data', function (error, filelist) {
      var title = 'WEB - create';
      var list = templateList(filelist);
      var template = templateHTML(
        title,
        list,
        `
        <form action="http://localhost:3000/create_process" method="post">
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
  }
```

2. "/create_process" 요청을 받기 위해 `else if(pathname === 'create_process')` 문을 추가한다.

```javascript
else if (pathname === '/create_process') {
    response.writeHead(200);
    response.end('success');
  }
```

3. POST 방식으로 전송된 데이터를 Node.js 안에서 가져온다. -> nodejs post data 검색

- Node.js 로 웹브라우저의 접속이 들어올 때마다 createServer() 의 callback 함수를 node.js가 호출한다.
- 이때 createServer()의 callback 함수의 인자로 request와 response가 있다.
  - request에는 요청할 때 웹 브라우저가 보낸 정보들이 담겨져 있다.
  - response에는 응답할 때 우리가 웹브라우저에게 전송할 정보들이 담겨져 있다.
- POST 방식으로 전송된 데이터를 가져오려면 사용자가 요청한 정보 안에 POST가 있으므로 request를 사용해야 한다.
- 웹 브라우저가 POST 방식으로 데이터를 전송할 때 데이터가 많으면 그 데이터를 한번에 처리하려 할 때 문제가 생길 수 있으므로 Node.js에서는 이 경우에 대비해서 아래와 같은 사용방법을 제공한다.
  - 큰 데이터에서 조각조각의 양들을 서버 쪽에서 수신할 때마다 `request.on('data', function(data){})` 의 callback 함수를 호출하며 이 callback 함수의 data 라는 인자를 통해 수신한 정보를 주기로 되어 있다. 그래서 이 callback 함수 내부에 `body = body + data;` 를 넣으면 정보를 수신받을 때마다 그 데이터를 body 변수에 추가로 저장할 수 있다.
  - 그러다가 더이상 들어올 정보가 없으면 `request.on('end', function(){})` 의 callback 함수를 호출하게 되어 있다. 이 callback 함수 내부에 `var post = qs. parse(body);` (이때 qs는 `var qs = require('queryString);`) 를 넣으면 post 변수에 {title : '입력한 title', description : '입력한 description'} 객체가 저장된다.

```javascript
var qs = require('querystring');

// ... (생략) ...

var app = http.createServer(function (request, response) {

// ... (생략) ...

  else if (pathname === '/create_process') {
    var body = '';
    request.on('data', function(data){
      body = body + data;
    });
    request.on('end', function(){
      var post = qs.parse(body);
      var title = post.title;
      var description = post.description;
    });
    response.writeHead(200);
    response.end('success');
  }

// ... (생략) ...
});
```
