# App 제작 - 출력정보에 대한 보안

## 보안 위험 요소 2. 오염된 정보가 나갈 때

### 문제 상황

create 창으로 들어가,

title :

```
XSS
```

description :

```
<script>
alert('merong');
</script>
```

를 제출한다면, 목록에 생성된 XSS 창으로 들어갈 때마다 merong 이라는 경고창이 뜰 것이다. `<script>` 태그가 들어가 있기 때문이다.

또는

```
<script>
location.href = 'https://opentutorials.org/course/1';
</script>
```

를 제출한다면 사용자가 XSS 창으로 들어갈 때마다 웹 브라우저는 이 링크로 사용자를 보내버릴 것이다.

또 이런 방식을 사용자의 로그인 정보를 갈취할 수도 있다.

### 해결 방안

많은 온라인 서비스들은 사용자로부터 입력받은 정보를 출력할 때는 그 정보에서 문제가 될 수 있는 것들을 필터링하는 작업을 많이 한다.

예를 들면, XSS 파일의 내용을 지워버릴 수 있다. 또는, XSS 의 `<script>` 의 꺾새를 그대로 화면에 출력할 수 있도록 < 는 `&lt;` 으로, > 는 `&gt;` 으로 바꾸어주면 된다.

이때 다른 사람이 만든 모듈을 사용해보자 -> npm sanitize 검색, 모듈 확인하고 평판 확인 sanitize-html은 최근 17만명이 다운로드 했으며, 다운로드 빈도수가 점점 높아지고 있으므로 많은 개발자들에게 이 모듈이 검증을 통과하고 있음을 짐작해볼 수 있다.

```
$ npm init
npm WARN config global `--global`, `--local` are deprecated. Use `--location=global` instead.
This utility will walk you through creating a package.json file.
It only covers the most common items, and tries to guess sensible defaults.

See `npm help init` for definitive documentation on these fields
and exactly what they do.

Use `npm install <pkg>` afterwards to install a package and
save it as a dependency in the package.json file.

Press ^C at any time to quit.
package name: (nodejs)
version: (1.0.0)
description:
entry point: (index.js)
test command:
git repository:
keywords:
author:
license: (ISC)
```

`npm init` 명령을 실행시키면 우리의 애플리케이션을 npm으로 관리하기 위한 절차가 시작된다.

package name 은 그냥 엔터를 하면 기본적으로 디렉토리 이름이 패키지 네임이 된다. 기본값은 모두 엔터를 쳐준다. 그러면 package.json 이라는 파일이 생기고, 우리의 프로젝트에 대한 정보가 생성된다.

그리고 이 상태에서 우리가 사용하고 싶은 패키지를 install한다.

```
$ npm install -S sanitize-html
```

-g 는 global의 약자로, 컴퓨터 전역에서 사용할 수 있는 독립적인 프로그램으로 까는 것이고,

-S 를 하면 우리가 진행하는 프로젝트에서 사용할 작은 부품으로써 깔게 된다.

모두 다운로드되면 node_modules 라는 디렉토리가 생기고 그 안에 sanitize-html 이 있다.

다시 한번 package.json 을 보면, "dependency" : { "sanitize-html" : "^1.18.2" } 로 되어 있는데, 이는 여러분의 애플리케이션이 sanitize-html 에 의존하고 있다는 뜻이다.

우리는 sanitize-html 만 다운받았는데도 node_modules 에 여러 파일들이 다운받아진 이유는, sanitize-html이 의존하는 모듈들과, 그 모듈들이 의존하는 모듈 등이 같이 다운받아졌기 때문이다. 이러한 복잡한 의존 관계를 npm 이 알아서 manage 해준다.

### sanitize-html 사용

공식 문서의 사용 예시를 참고해

```javascript
var sanitizeHTML = require('sanitize-html');
```

코드를 추가하고,

```javascript
fs.readFile(
          ...
          function (err, description) {
            var title = queryData.id;
            var sanitizedTitle = sanitizeHTML(title); // 이처럼 변수를 만들면 변수 이름을 통해 sanitized된 정보인지 확인 가능해진다.
            var sanitizedDescription = sanitizeHTML(description);
            var list = template.list(filelist);
            var html = template.HTML(
              sanitizedTitle,
              list,
              `<h2>${sanitizedTitle}</h2>${sanitizedDescription}`,
              `<a href="/create">create</a>
              <a href="/update?id=${sanitizedTitle}">update</a>
              <form action="delete_process" method="post">
              <input type="hidden" name="id" value="${sanitizedTitle}">
              <input type="submit" value="delete">
              </form>`
            );
            ...
          }
        );
```

이처럼 코드를 수정한다.

그러면 `<script>` 태그가 있는 문서를 create하여, 그 태그가 포함된 파일이 저장된다 하더라도, 그 파일을 읽어 화면에 출력할 때는 `<script>` 와 같이 예민한 태그와 태그 안의 내용이 지워진 채로 출력된다.

sanitizeHtml을 호출할 때 두번째 인자로 객체를 주어 허용되는 태그를 지정할 수도 있다.

```javascript
var sanitizedDescription = sanitizeHTML(description, {
  allowedTags: ['h1'],
});
```
