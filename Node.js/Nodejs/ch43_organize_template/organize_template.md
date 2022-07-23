# App 제작 - 템플릿 기능 정리정돈하기

## 객체란?

서로 연관된 데이터와 함수를 그룹핑해서 코드의 복잡성을 낮추는 수납 상자.

templateHTML 과 templateList 는 모두 template 라는 공통된 접두사를 가지고 있다. 서로 성격이 같을 때 이처럼 접두사나 접미사를 사용하기도 하지만, 이보다는 객체를 통해 정리정돈하는 것이 더 좋을 수 있다.

template 라는 객체를 만들어보자.

```javascript
var template = {
  html: function (title, list, body, control) {
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
  },
  list: function (filelist) {
    var list = '<ul>';
    var i = 0;

    while (i < filelist.length) {
      list += `<li><a href="/?id=${filelist[i]}">${filelist[i]}</a></li>`;
      i += 1;
    }

    list = list + '</ul>';
    return list;
  },
};

// var list = templateList() -> var list = template.list()
//var template = templateHTML() -> var html = template.html()
```

## refactoring

동작 방법은 똑같지만 내부의 코드를 더 효율적으로 바꾸는 행위.

이것이 중요하다. 처음부터 함수 등을 이용해 코드를 짜는 것은 어려운 일이기 때문.

알고 있는 최소한의 문법으로 좀 불편하지만 잘 동작하는 코드를 짠 다음 자주 자주 리팩토링을 하라. (함수화, 객체화, 배열화 등)
