var memberArray = ['egoing', 'graphittie', 'leezche'];
console.log('memberArray[2]', memberArray[2]);
console.group('array loop');
var i = 0;
while (i < memberArray.length) {
  console.log(i, memberArray[i]);
  i = i + 1;
}
console.groupEnd('array loop');
// ��ü�� �̸��� �ִ� ������ ��������
var memberObject = {
  manager: 'egoing',
  developer: 'graphittie',
  designer: 'leezche',
};
console.group('object loop');
for (var name in memberObject) {
  console.log(name, memberObject[name]);
}
console.groupEnd('object loop');
