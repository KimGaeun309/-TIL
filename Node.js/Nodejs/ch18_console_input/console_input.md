# �ֿܼ����� �Է°�

���α׷��̶� � **�Է�(INPUT)** �� ���ؼ� ������ ó���� �� �� ����� **���(OUTPUT)** �ϴ� ����̴�.

�׷��� �� �Է�(INPUT)�� �θ��� ���� ǥ����� Parameter, Argument ���� �ִ�.

- Parameter : �ԷµǴ� ������ ����
- Argument : �� ���Ŀ� �°� ������ �Է��� ��

�Է°� ��¿��� ���� ������ ������ �̹� �ð����� �ֿܼ��� �Է� ���� �ִ� ����� ���캼 ���̴�.

**�ܼ� �Է°�** �� ���� ���α׷� ���ο��� **���ǹ�** �� ����Ͽ� �ٸ� output�� ����ϴ� ���α׷��� ������.

-> nodejs console input parameters �˻�

## conditional.js

```javascript
var args = process.argv;

console.log(args);
```

�� �ڵ带 �����ϸ�

```javascript
[
  'C:\\Program Files\\nodejs\\node.exe', // node.js runtime�� ��ġ
  'C:\\Users\\mihar\\Programming\\Nodejs\\ch18_console_input\\conditional.js', // �츮�� �����Ų ������ ���
  'k8805', // �츮�� �ܼ� �Է°�
];
```

�̿� ���� ����� ���´�.

## ���

�츮�� `var args = process.argv;` �� �� ���� `args[2]` �� ù ��° �ܼ� �Է°��� ������ �� �ְ�, `args[3]` ���� �� ��° �ܼ� �Է°��� ������ �� �ִ�.
