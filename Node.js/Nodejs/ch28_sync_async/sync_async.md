# 동기와 비동기

학습 목표: synchronous & asynchronous 의 차이와 의미 알기

## synchronous

어떤 일을 할 때 한 가지 일을 마쳐야 다음 일을 할 수 있음. -> 동기적인 처리

## asynchronous

어떤 일이 너무 시간이 오래 걸릴 때 그 작업을 다른 쪽에 맡기고 다음 일을 시작하여 여러 일을 동시에 처리해 시간을 효율적으로 사용 -> 병렬적으로 처리 -> 비동기적인 처리

## sync 와 async 차이 확인

- Node.js는 이 비동기적 처리(병렬적 처리)를 하기 위한 기능들을 가지고 있다.
- 비동기란 무엇인지 코드 레벨에서 살펴보자. (비동기는 효율적이지만 매우 복잡하여 어렵게 느껴질 수 있다.)
- Node.js의 공식 문서를 확인해보면 fs.link(), fs.linkSync(), fs.lstat(), fs.lstatSync(), fs.readFile(), fs.readFileSync() 등 뒤에 Sync가 붙은 것과 그렇지 않은 것이 있음을 확인할 수 있다.

### fs.readFileSync(path[, options])

```javascript
console.log('A');
var result = fs.readFileSync('ch28_sync_async/sample.txt', 'utf8');
console.log(result);
console.log('C');
```

동기적 처리를 하는 함수를 실행시키면 A, B, C 가 순서대로 출력된다.

### fs.readFile(path[, options], callback)

```javascript
console.log('A');
fs.readFile('ch28_sync_async/sample.txt', 'utf8', function (err, result) {
  console.log(result);
});
console.log('C');
```

비동기적 처리를 하는 함수를 실행시키면 A, C, B 이렇게 출력된다.

## callback

fs.readFile에는 fs.readFileSync 와 다르게 callback이 있다.
readFile() 에서 파일 읽기를 한 다음 callback으로 준 function 이 실행된다.

```javascript
var a = function () {
  console.log('A');
};

function slowfunc(callback) {
  callback();
}

slowfunc(a);
```

위 코드에서는 slowfunc() 가 callback을 받는다. 그리고 slowfunc()에서는 작업이 끝난 후 callback을 실행시켜준다. 따라서 `slowfunc(a);` 를 실행시키면 slowfunc()에 callback으로 a 라는 함수를 주게 되므로, slowfunc() 에서 a 함수가 실행되어 A 가 출력된다.
