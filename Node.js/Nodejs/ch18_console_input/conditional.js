var args = process.argv;

// console.log(args);
// [
//   'C:\\Program Files\\nodejs\\node.exe', // node.js runtime�� ��ġ
//   'C:\\Users\\mihar\\Programming\\Nodejs\\ch18_console_input\\conditional.js', // �츮�� �����Ų ������ ���
//   'k8805' // �츮�� �ܼ� �Է°�
// ]

console.log('A');
console.log('B');
if (args[2] === '1') {
  console.log('C1');
} else {
  console.log('C2');
}
console.log('D');
