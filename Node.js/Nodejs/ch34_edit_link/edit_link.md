# App 제작 - 글 수정: 글 수정 링크 생성

앞에서 생성 기능을 만들었으니 이제 수정 기능을 만들어보자.

create 옆에 update 링크를 두되, Home에서는 update 링크가 나타나지 않도록 해보자.

create와 update 링크를 만드는 html 또한 templateHTML() 에 인자로 넘겨받아 만들도록 바꾸어보자.

```javascript
function templateHTML(title, list, body, control) {
  return `
  <!doctype html>
  <html>
    <head>
      <title>WEB1 - ${title}</title>
      <meta charset="utf-8">
    </head>
    <body>
      <h1><a href="/">WEB1</a></h1>
      ${list}
      ${control}
      
      ${body}
    </body>
    </html>
  `;
}
```
