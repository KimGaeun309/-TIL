# App 제작 - Not found 구현

``` javascript
 console.log(url.parse(_url, true));
```
를 실행해보면 

``` javascript
  Url {
    protocol: null,
    slashes: null,
    auth: null,
    host: null,
    port: null,
    hostname: null,
    hash: null,
    search: '?id=HTML',
    query: [Object: null prototype] { id: 'HTML' },
    pathname: '/', // pathname은 query string이 포함되지 않은 경로
    path: '/?id=HTML', // path에는 query string이 포함된 경로
    href: '/?id=HTML'
  }
```
이러한 출력 결과를 확인할 수 있다. 

* url.parse() 가 반환하는 객체의 pathname : query string이 포함되지 않은 경로
* url.parse() 가 반환하는 객체의 path : query string이 포함된 경로

따라서, 우리는 pathname 을 확인하여 올바르지 않은 경로인 경우 "Not found" 를 나타내도록 조건문을 구성할 수 있다. (자세한 코드는 ch19_use_conditional/main.js 참고)

# App 제작 - 홈페이지 구현
현재 WEB 을 클릭하면 undefined 만 출력된다.
