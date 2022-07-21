# App ���� - Not found ����

``` javascript
 console.log(url.parse(_url, true));
```
�� �����غ��� 

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
    pathname: '/', // pathname�� query string�� ���Ե��� ���� ���
    path: '/?id=HTML', // path���� query string�� ���Ե� ���
    href: '/?id=HTML'
  }
```
�̷��� ��� ����� Ȯ���� �� �ִ�. 

* url.parse() �� ��ȯ�ϴ� ��ü�� pathname : query string�� ���Ե��� ���� ���
* url.parse() �� ��ȯ�ϴ� ��ü�� path : query string�� ���Ե� ���

����, �츮�� pathname �� Ȯ���Ͽ� �ùٸ��� ���� ����� ��� "Not found" �� ��Ÿ������ ���ǹ��� ������ �� �ִ�. (�ڼ��� �ڵ�� ch19_use_conditional/main.js ����)

# App ���� - Ȩ������ ����
���� WEB �� Ŭ���ϸ� undefined �� ��µȴ�.
