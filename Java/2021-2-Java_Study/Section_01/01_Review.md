# Section 01
## Java 클래스
### 우리는 객체를 지향한다
* Object-Oriented Programming, OOP
* Java, C++, C#, Object-C 등
* 제일 중요한 건 **객체(Object)**
### 객체
* 이 세상에 존재하는 것을 아무거나 하나 집어도 객체일 확률 99%
* 객체는 내가 작헝한 class에 숨을 불어넣어 (new, 메모리에 할당) 만든다.
* 객체는 정보(변수)와 행동(메소드)를 가진다.
### 절차지향 vs 객체지향
* 절차지향
```C
// fight 라는 함수
int fight() {
  int enemyHP = 100;
  int enemyATK = 5;
  int playerHP = 100;
  
  // 적 공격
  enemyHP -= playerATK;
  
  if (enemyHP <= 0) return 0;
  
  // 플레이어 피격
  playerHP -= enemyATK;
  
  if (playerHP <= 0) return 1;
  ...
  ...
}
```
* 객체지향 - 더 생산성이 높다!
```java
fight() {
  player.attack(enemy);
  enemy.attack(player);
}

class Player
{
  int hp;
  int atk;
  attack();
}

class Enemy
{
  int hp;
  int atk;
  attack();
}
```

### The WITCHER 캐릭터 객체
```java
class Player {

  String name = "Ciri";
  Color hairColor;
  
  // 특징
  int height;
  int weight;
  
  // 행동돌
  void Walk()
  int Attack()
  void Talk()
  
  class Color ( // 클래스 안에 또 클래스
    int r;
    int g;
    int b;
  }

}
```
## Java 상속
### 부모와 자식
* 클래스는 부모와 자식 관계를 가질 수 있다.
* 자식 클래스는 부모 클래스(super class)가 물려준 재산(변수와 메소드)을 상속받는다.
* 모든 클래스는 Object(root of the class hierarchy)라는 최상위 클래스를 상속받는다.
### Object의 유산
**ex.**a Monster 클래스와 Hero 클래스가 Unit 클래스를 상속
```java
class Unit {
  String Name;
  int HP;
}

class Monster extends Unit {
  void Attack();
  void Run();
}

class Hero extends Unit {
  void Attack();
  void Upgrade();
}
```
## Java 예외처리
### 예외는 있는 법
* 특정 메소드는 실패할 경우가 있다
* 인터넷이 끊겼거나, 사용자의 입력값이 이상할 때 등등
* 실패 했을 때 자연스럽게 대처하는 코드를 작성한다
### try, catch, (finally)
try에 따라 Method1 수행하다가 exception이 발생하면 catch 부분이 실행되어 경고 메시지가 뜬다.
```java
try {
  Method1();
}
catch (Exception e) {
  showAlert(e.getMessage());
}

void Method1() throws Exception {
  if (isInternetOff) {
    throw new Exception("인터넷안됨"); // Exception 의 생성자에 "인터넷안됨" 메시지를 던져줌
  }
  else if (isWrongInput) {
    throw new Exception("잘못된입력");
  }
}
```
### 좋은 예
: 카카오톡 메세지 - 대기열(?)
```java
String msg = "잘 지내?";

try {
  SendMessage(msg);
}
catch (NetwordException e) {
  AddSchedule(msg);
}
```
### try ~ catch 사용하는 이유
: 예측할 수 없는 상황에 프로그램이 직면했을 때 무슨 문제가 일어났는지를 알려주거나 대체할 동작을 수행하도록 하기 위해.

## Java interface 파트1 - 다중상속
### 인터페이스의 쓰임새
* UI(유저 인터페이스) 아님!!
* 두 가지로 나뉨
  + 다중 상속 (파트1)
  + 콜백 메소드 (파트2)

### 다중 상속?
* Java 에서는 2개 이상의 상속이 불가능하다
* '상속(*extends*)' 대신 '구현(*implements*)'하자.
* 뭐로? 인터페이스로!
### Object의 유산
Attackable 이라는 인터페이스를 만들어 몬스터와 플레이어에 구현... Attack()
Tradable 이라는 인터페이스를 만들어 상점주인과 플레이어에 구현... Sell(), Upgrade()
### 상속과 구현의 차이
* extends, 상속은 아이덴티티를 보유한다.
  + 개는 동물이다, 사람은 포유류다
* implements, 구현은 역할(Role)을 부여한다.
  + 개는 애완동물이다, 이 사람은 프로그래머다
* implements, '구현'은 변수를 상속받지 않는다. 오로지 메소드만(행동만) 가지고 있다.

## Java interface 파트2 - 콜백
### CALL BACK
* 사용자가 버튼을 눌렀을 때 뭔가 하고싶어.
* 앱을 사용하다가 홈버튼을 누르면 어떻게 처리하지?
* 다운로드가 완료되었으면 알림을 울릴 수 없을까?

```java
// OnDownloadListener 라는 인터페이스에 onDownloadFinish 라는 메소드가 정의되어 있었음.
// 시점을 나타낸다!

public cass Downloader implements OnDownloadListener { 
  void Start() {
    Download(this); // this 는 Downloader 도 되고 OnDownloadListener 도 되지만 이 코드에서는 후자의 형태로 들어감.
  }
  
  void Download(OnDownloadListener listener) {
    // Downloading...
    listener.onDownloadFinish();
  }
  
  @Override
  public void onDownloadFinish() {
    Message("다운로드 완료!");
  }
}
```
### 어떤게 콜백이지?
* 콜백 메소드는 보통 onClick, onTouch, onPressed 등 on~ 이 붙는다.
* 콜백을 정의한 인터페이스는 보통 OnClickListener, OnTouchListener 등 Listener 가 많이 붙는다.

## 마무리
1. 클래스
2. 상속
3. 인터페이스
4. 예외처리

***
* Class는 객체를 만드는 청사진과 같다.
```java
  public class Human

  Human me = new Human();
//클래스 객체 생성자
```
* Class extends
클래스는 단 하나의 부모만 가질 수 있다. 그 부모는 조부모를 가질 수 있다.
``` java
public class Animal extends Life

public class Human extends Animal
```
* interface
인터페이스는 클래스 하나에 1개 이상 구현 가능(상속과 다름)
인터페이스는 콜백 메소드를 만들 수 있다.
```java
public class Human extends Animal implements Programmer, Gamer, FoodFighter
```
* 예외처리
실패할 가능성이 있는 메소드들이 다수 존재한다. try로 시도하고 catch로 대응하자

