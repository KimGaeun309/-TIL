var memberArray = ['egoing', 'graphittie', 'leezhce'];
console.log('memberArray[2]', memberArray[2]);

// ��ü�� �̸��� �ִ� ������ ��������
var memberObject = {
  manager: 'egoing',
  developer: 'graphittie',
  designer: 'leezhce',
};
// ��ü�� ���� update
memberObject.designer = 'leezche';
// ��ü�� ���� ���� . �̳� [] �� ���
console.log('memberObject.designer', memberObject.designer);
console.log("memberObject['designer']", memberObject['designer']);
// ��ü�� ���� ����
delete memberObject.manager;
console.log('after delete memberObject.manager', memberObject.manager);
