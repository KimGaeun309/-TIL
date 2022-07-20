var memberArray = ['egoing', 'graphittie', 'leezhce'];
console.log('memberArray[2]', memberArray[2]);

// 객체는 이름이 있는 정보를 정리정돈
var memberObject = {
  manager: 'egoing',
  developer: 'graphittie',
  designer: 'leezhce',
};
// 객체의 내용 update
memberObject.designer = 'leezche';
// 객체를 읽을 때는 . 이나 [] 를 사용
console.log('memberObject.designer', memberObject.designer);
console.log("memberObject['designer']", memberObject['designer']);
// 객체의 내용 삭제
delete memberObject.manager;
console.log('after delete memberObject.manager', memberObject.manager);
