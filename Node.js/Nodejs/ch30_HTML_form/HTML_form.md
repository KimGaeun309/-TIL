# HTML-form

- 현재 프로그램으로는 컨텐츠 생성을 이 사이트의 소유자만 할 수 있다.
- 누구나 웹을 통해 데이터를 전송할 수 있게 하고자 한다면 컨텐츠를 사용자가 웹을 통해 생성하고 수정하고 삭제하는 방법을 살펴보아야 한다.
- 사용자가 서버 측으로 데이터를 전송하기 위한 방식인 HTML 을 form 에 대해 알아보자.

```HTML
<form action="http://localhost:3000/process create">
  <p>
    <input type="text" name="title" />
  </p>

  <p>
    <textarea name="description"></textarea>
  </p>

  <p>
    <input type="submit" />
  </p>
</form>
```

위와 같이 만들고, 만들어진 웹 사이트에서 title과 description에 각각 정보를 적어 submit 버튼을 클릭하면 localhost:3000 에 입력한 정보가 query string으로 만들어져 링크가 생성된다.

하지만 이는 좋은 방법은 아니다. 주소에 데이터에 포함되어 있다면 다른 사람이 그 링크에 접속했을 때 서버에 있는 데이터가 수정되거나 삭제될 수 있다.

즉, 서버에서 데이터를 get 할 때는 query string 을 사용하면 되지만, 서버의 데이터를 수정 or 삭제할 때에는 눈에 보이지 않는 방식으로 데이터를 전송해야 한다.

이러기 위해서는

```HTML
<form action="http://localhost:3000/process create" method = 'post'>
  <p>
    <input type="text" name="title" />
  </p>

  <p>
    <textarea name="description"></textarea>
  </p>

  <p>
    <input type="submit" />
  </p>
</form>
```

이와 같이 `method="post"` 라는 코드를 추가하면 정보가 query string에 들어가지 않는다.

이런 방식으로 데이터를 전송할 경우 보다 큰 데이터도 전송할 수 있다. (URL로 전송할 수 있는 정보에는 한계가 있다.)

반면, 서버로부터 사용자가 데이터를 get 할 때에는 `method = "get"` 으로 되어 있거나 method 가 생략되어 있다.

하지만 서버의 데이터를 수정 삭제 할 때에는 반드시 method를 post 방식으로 해야 한다.
