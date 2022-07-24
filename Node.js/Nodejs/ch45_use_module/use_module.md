# App 제작 - 모듈의 활용

1. lib/template.js 파일 만들어 template 객체 두기

```javascript
module.exports = {
  HTML: function (title, list, body, control) {
    ...
  }
   list: function (filelist) {
    ...
   }
```

2. main.js에서 require()로 lib/template.js 모듈 가져오기

```javascript
var template = require('./lib/template.js');
```
