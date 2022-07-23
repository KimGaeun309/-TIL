# App 제작 - 글 삭제: 삭제 버튼 구현

삭제 버튼을 링크로 만드는 것은 대단히 잘못된 것이다. 링크는 클릭하면 이동하는데, 이 주소를 copy해서 누군가에게 보낼 수 있기 때문이다.

> 구글에서 만든 어떤 플러그인이 사용자들이 어떤 페이지를 클릭하면 빠르게 갈 수 있도록 미리 페이지를 다운받는 캐싱이라는 기능을 가지고 있었다. 그 플러그인이 활성화된 상태로 사용자가 웹 페이지에 들어왔는데 delete를 GET 방식으로 (querystring이 들어가 있으면 GET 방식이다) 구현해두었더니 이 플러그인이 이 링크를 통해 들어가서 삭제되는 문제가 있었다.

따라서 삭제 부분은 form으로 구현할 것이다.

```javascript
var template = templateHTML(
  title,
  list,
  `<h2>${title}</h2>${description}`,
  `<a href="/create">create</a>
    <a href="/update?id=${title}">update</a>
    <form action="delete_process" method="post">
    <input type="hidden" name="id" value="${title}">
    <input type="submit" value="delete">
    </form>`
);
```

이렇게 구현하면 delete 버튼을 클릭했을 때 "/delete_process" 로 이동하는 것을 볼 수 있다.
