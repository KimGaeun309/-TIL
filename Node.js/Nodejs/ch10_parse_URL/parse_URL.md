# URL�� ���ؼ� �Էµ� �� ����ϱ�

`http://localhost/?id=HTML`

`id=HTML` �κ��� query string�̶� �ϴµ�, �̿� ���� �ٸ� ������ �����ִ� ���� �غ���.

## main.js

- ���� URL�� `localhost:3000/3.html` �̴�.
- �̸� `localhost:3000/?id=JavaScript` �� ������ 3.html �������� �����ֵ��� �����غ���.
- `id=JavaScript` �� request.url �� �ݿ��ȴ�.
- �� �̷κ��� �����͸� ������ �� �־�� �Ѵ�.
- nodejs url parse query string �˻�

`var url = require('url');` -> url �̶�� ��� ���

`var queryData = url.parse(_url, true).query;` -> query string�� ��ü�� �޾� ���
