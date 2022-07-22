// readFile() 와 readFileSync() 를 비교

var fs = require('fs');

/*
console.log('A');
var result = fs.readFileSync('ch28_sync_async/sample.txt', 'utf8'); // -> A B C 출력
console.log(result);
console.log('C');
*/

console.log('A');
fs.readFile('ch28_sync_async/sample.txt', 'utf8', function (err, result) {
  // -> A C B 출력
  // callback이 함수로 쓰여짐
  console.log(result);
});
console.log('C');
