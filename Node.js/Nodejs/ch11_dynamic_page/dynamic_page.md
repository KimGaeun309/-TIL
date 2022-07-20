# 동적인 웹페이지 만들기

- query string 에 따라서 다른 완성된 웹페이지를 표현하도록 해보자.

```javascript
var title = queryData.id;

var template = `
  <!doctype html>
<html>
<head>
  <title>WEB1 - ${title}</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="/">WEB</a></h1>
  <ol>
    <li><a href="/?id=HTML">HTML</a></li>
    <li><a href="?id=CSS">CSS</a></li>
    <li><a href="?id=JavaScript">JavaScript</a></li>
  </ol>
  <h2>${title}</h2>
  <p><a href="https://www.w3.org/TR/html5/" target="_blank" title="html5 speicification">Hypertext Markup Language (HTML)</a> is the standard markup language for <strong>creating <u>web</u> pages</strong> and web applications.Web browsers receive HTML documents from a web server or from local storage and render them into multimedia web pages. HTML describes the structure of a web page semantically and originally included cues for the appearance of the document.
  <img src="coding.jpg" width="100%">
  </p><p style="margin-top:45px;">HTML elements are the building blocks of HTML pages. With HTML constructs, images and other objects, such as interactive forms, may be embedded into the rendered page. It provides a means to create structured documents by denoting structural semantics for text such as headings, paragraphs, lists, links, quotes and other items. HTML elements are delineated by tags, written using angle brackets.
  </p>
</body>
</html>
  `;

response.end(template);
```

- 위와 같은 방법으로 정보를 dynamic하게 programming 적으로 생성할 수 있게 되었다.
- 이를 통해 웹사이트의 순서가 있는 리스트를 순서가 없는 리스트로 바꾸고자 할 때 template 의 코드만 바꾸어도 동시에 바뀌는 효과를 가질 수 있다.

- 이때 제목 부분은 동적으로 바꿀 수 있지만 본문은 정적인 상태이다. 이는 파일에 본문만 저장해 두었다가 사용자의 요청에 해당되는 파일의 본문만을 읽어서 여기에 가져다놓는 식으로 하여 해결할 수 있다. 다음 시간에 살펴보자.
