var args = process.argv;

// console.log(args);
// [
//   'C:\\Program Files\\nodejs\\node.exe', // node.js runtime의 위치
//   'C:\\Users\\mihar\\Programming\\Nodejs\\ch18_console_input\\conditional.js', // 우리가 실행시킨 파일의 경로
//   'k8805' // 우리의 콘솔 입력값
// ]

console.log('A');
console.log('B');
if (args[2] === '1') {
  console.log('C1');
} else {
  console.log('C2');
}
console.log('D');
