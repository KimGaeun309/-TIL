# Section 04
## 안드로이드 Fragment
### Fragment (조각)
* 만들어진 의도: 유연한 UI 제공(다양하게 활용)
* 작은 Activity
* Activity 를 부모처럼 가진다
* 1 Activity, Multiple Fragment
#### 고유의 생명주기
* 부모 Activity 의 생명주기를 거의 따름.
* 보통 onCreateView()에서 코드 시작.

### Fragment 생성 방법
1. XML
2. Java
### XML 생성 기법
* name에 클래스 명 적고 만들면 영원히 박제해버린다
* 실행 시에 바꿀 수가 없다
* 고정으로 쓸 때 편하다

### Java 생성 기법
* XML 에는 들어갈 장소만 만들어둔다
* 코드로 만든다
* 언제든 다른 Fragment로 교체 가능하다

## 안드로이드 ViewPager
### ViewPager
* 좌우로 스와이프하여 여러 페이지를 이동할 때 쓰인다.
* 상단이나 하단에 탭과 연동하여 많이 쓰인다.
* 하나의 페이지는 보통 Fragment로 구현한다

### Adapter
* Data - 정보의 집합
* Adapter (클래스)
* AdapterView (변환)

## 안드로이드 Shared Preference
### Shared Preference
* 파일을 간단하게 저장할 때 쓰는 것
* Android가 제공하는 간단한 값 저장기능
* 키워드 - 값 형태로 저장하고 불러온다
* 앱의 알림, 소리, 진동 On/Off, 앱의 최초실행 유무 등
* 설정 값을 저장할 때 많이 쓰임

### Key - Value
* 자료구조의 일환







