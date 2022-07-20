# Node.js로 웹서버 만들기

## Web Browser 와 Web Server의 관계

: 웹 브라우저에 주소를 입력해 요청을 하면 웹 서버는 그 정보를 찾아 응답해준다.

## Web Server 로써의 Node.js

: 우리가 지금부터 살펴볼 Node.js 는 Apache 와 같이 웹 서버로도 사용될 수 있다. 그러한 특성을 이용하면 Apache로는 할 수 없는 일을 할 수 있다. 그를 위한 코드를 살펴보고 Node.js로 웹 서버를 구동시켜보자.

<a url="https://opentutorials.org/module/3549/21032">오픈튜토리얼(예제코드)</a>

위 사이트의 코드를 가져와서 main.js를 실행시킨 다음 웹 url 로 localhost:3000 을 입력하면 웹 페이지가 나타난다.

이때, Node.js 가 Web Server로 사용되는 중이다.

> `response.end(fs.readFileSync(__dirname + url));`
>
> 라는 코드가 있는데, 이는 이 \_\_dirname + url 은 우리가 읽어야 할 파일 경로이다.
>
> - 사용자가 접근할 때마다 javascript를 통해서 우리가 읽어들여야 할 파일을 만들고 그것을 file로부터 read한다.
> - 위 readFileSync() 명령에 node.js 의 기능이 있어서 node.js 가 이 경로의 파일을 읽어 그 값을 가져온다.
> - 그리고 response.end() 안에 그 값을 위치시키면 사용자에게 그 데이터를 보여준다.
> - 즉, node.js는 response.end() 안에 어떤 코드를 넣느냐에 따라 사용자에게 전송하는 데이터가 바뀐다.
> - 이것이 Apache는 할 수 없고, node.js나 php나 python django 가 할 수 있는 일이다.
>
> 즉 프로그래밍적으로 사용자에게 전송할 데이터를 생성하는 것이 node.js가 가진 힘이다.
