# Section 02
[AndroidDeveloper](https://developer.android.com/)
## 액티비티
### 어플리케이션 Component
+ 안드로이드 삼대장
  * ContentProvider
  * Service
  * BroadcastReceiver
+ 원수
  * Activity
### 액티비티는?
+ 액티비티 = 알파, 오메가
  * 윈도우의 '창'
  * 맥의 'finder'
  * 아이콘 누르면 뜨는 것 = 액티비티
+ 액티비티 = 화면
  * UI를 보여주고
  * 행동까지 한다
  * 어플리케이션에서 하는 일은 다 한다
### 액티비티의 생명주기
**외우자**    
on이 붙은 것은 인터페이스의 콜백.
## Intent
### intent는 우편배달부
* 액티비티 - 액티비티
* 앱 - 앱
#### 명시적 Intent
* 보낸이와 받는이가 명시되어있다.
``` java
Intent intent = new Intent(this, NewActivity.class);
startActivity(intent);
```
 #### 암시적 Intent
 * 해당된다 싶으면 다 부른다.
 ``` java
 Intent intent = new Intent();
 sendIntent.setAction(Intent.ACTION_CALL);
 startActivity(sendIntent);
 ```

