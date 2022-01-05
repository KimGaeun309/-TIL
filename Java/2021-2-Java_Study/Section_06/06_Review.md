# Section 06
## Multi Thread
### Thread
* 작업의 흐름
* 지금까지 우리가 만든 앱은 하나의 Thread를 타고 실행중
* 기본적으로 'main' 혹은 'UI' Thread가 존재한다.

### Multi threading
왜?
많고 무거운 일을 해야할 때 이를 보다 작은 일들로 나누는 게 더 좋을 수 있음. (분업)
하지만 CPU의 클럭, 속도에는 한계가 있다. 빠른속도로 다양한 일을 하기에 동시에 되는 것처럼 보이는 것.

### Android Threading
<방법1>
* UI Thread
  + UI Drawing
  + Touch Event
  + Huge Calculation
  + Internet
-> 렉이 걸릴 수 있음
<방법2>
* UI Thread
  + UI Drawing
  + Touch Event
* worker Thread #-
  + Huge Calculation
  + Internet
-> UI와 이벤트 일 / 인터넷 연결과 복잡한 연산 으로 분할됨.
### Thread의 2가지 구현법
1. Java 의 Thread 클래스와 android 의 Handler 클래스 -> Thread에서 일을 다 하면 Handler에 반영
2. android의 AsyncTask 클래스 -> Thread 와 Handler 를 통합.

## AsyncTask
### AsyncTask
* 간단하게 새로운 쓰레드를 생성에서 작업할 수 있음
* 코드도 간결해서 많이 쓰임
* 초보들에게 강추

### 사용법
``` java
public void onClick(Viewv) {
  new DownloadImageTask().execute("http://example.com/image.png");
}

private class DownloadImageTask extends AsyncTask<String, Void, Bitmap> {
  /* The system calls this to perform work in a worker thread and
     delivers it the parameters given to AsyncTask.execute() */
  protected Bitmap doInBackground(String... urls) {
    return loadImageFromNetwork(urls[0]);
  }
  
  /* The system calls this to perform work in the UI thread and delivers
     the result from doInBackground() */
  protected void onPostExecute(Bitmap result) {
    mImageView.setImageBitmap(result);
  }
}

// doInBackground 와 onPostExecute 는 서로 다른 쓰레드에서 실행됨.
```

## 이미지 라이브러리들
### 이미지를 그냥 넣으면 안되는 이유
* 서버에서 수많은 이미지를 다운로드할 수 있어야 한다
  + HTTP Client 기능
* 다시 불러오지 않아야 한다
  + 디스크, 메모리 캐시 기능 -> 보통 LRU Cache 사용..
* 고해상도 이미지를 줄여서 메모리를 효율적으로 쓴다 
  + 이미지 처리 기능
### 이미 만들어진 걸 쓼 수 있다
* Glide
* Volley
* AUIL
* Picasso




