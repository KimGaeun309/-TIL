# 콘솔에서의 입력값

프로그램이란 어떤 **입력(INPUT)** 에 대해서 정보를 처리한 후 그 결과를 **출력(OUTPUT)** 하는 기계이다.

그래서 저 입력(INPUT)을 부르는 여러 표현들로 Parameter, Argument 등이 있다.

- Parameter : 입력되는 정보의 형식
- Argument : 그 형식에 맞게 실제로 입력한 값

입력과 출력에도 여러 종류가 있지만 이번 시간에는 콘솔에서 입력 값을 주는 방법을 살펴볼 것이다.

**콘솔 입력값** 에 따라 프로그램 내부에서 **조건문** 을 사용하여 다른 output을 출력하는 프로그램을 만들어보자.

-> nodejs console input parameters 검색

## conditional.js

```javascript
var args = process.argv;

console.log(args);
```

위 코드를 실행하면

```javascript
[
  'C:\\Program Files\\nodejs\\node.exe', // node.js runtime의 위치
  'C:\\Users\\mihar\\Programming\\Nodejs\\ch18_console_input\\conditional.js', // 우리가 실행시킨 파일의 경로
  'k8805', // 우리의 콘솔 입력값
];
```

이와 같은 결과가 나온다.

## 결론

우리는 `var args = process.argv;` 를 한 다음 `args[2]` 로 첫 번째 콘솔 입력값에 접근할 수 있고, `args[3]` 으로 두 번째 콘솔 입력값에 접근할 수 있다.
