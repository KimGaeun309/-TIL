# App ���� - ������ �̿��� ���� ����

query string�� ���� ������ ����Ǵ� �� ���ø����̼��� ������.

```javascript
fs.readFile(`data/${queryData.id}.txt`, 'utf8', function (err, description) {
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
  <p>
    ${description}
  </p>
</body>
</html>
  `;
    response.end(template);
  });
});
```

���� ���� ������� ������ �����Ѵ�.
�̶� data ���丮 �ȿ� �ִ� ������ ������ �����ϸ� main.js �� ������ ����� �ٽ� �������� �ʾƵ� ���ΰ�ħ�ϸ� �ٷ� �ݿ��ȴ�.

Ŭ���̾�Ʈ�� ��û�� ���� ������ ���� ������ �ҷ����� �����̴�.
