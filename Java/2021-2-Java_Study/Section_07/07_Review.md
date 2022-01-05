# Section 07
## 서버와 클라이언트
### 서버
: 사용자들이 올린 글, 사진, 리플 등이 서버에 저장된다.
### 클라이언트
: 사용자의 요청을 보내고 서버의 응답을 사용자에게 보여주는 매개체.
보통 안드로이드 앱을 개발한다는 건 클라이언트를 개발한다는 뜻.
### 서비스를 만드는데 서버를 모를 때
-> 포기하거나 외주를 맡기거나 싱글플레이 게임개발로 전향하거나 서버를 배운다
### 서버 - 클라이언트
클라이언트 -Request-> 서버      
서버 -Quiry->데이터베이스      
서버 <-Fetch-데이터베이스      
(+) Data Stroage / CDN (데이터 저장) 도 따로 있다.       
클라이언트 <-Response- 서버      
* History of Internet
## Request, Response
### HTTP
인터넷 주소창 http://www.goolgle.com 에서
* http:// 는 방식. 통신 규약을 표현.
* google.com 은 서버의 도메인 주소. 우리가 요청하는 값.
### HTTP Request - GET
: 있는 자료를 요청할 때. 
### HTTP Request - POST
: 내 자료를 보낼 때.
### HTTP Response
: 코드로 처리가 어떻게 되었는지 알려줌.
### http://square.github.io/okhttp
## JSON
### JSON
* HTTP가 상호 통신의 규약이라면 JSON은 자료 교환의 규약이다. (제약은 없음)      
* Key-Value 형태의 구조
* 가벼워서 모바일 환경에서 선호.
```
{
  "이름": "테스트",
  "나이": 25,
  "성별": "어",
  "주소": "서울특별시 양천구 목동",
  "특기": ["농구", "도술"],
  "가족관계": {"#":2, "아버지":"홍판서", "어머니":"춘섬"},
  "회사": "경기 안양시 만안구 안양7동"
}
```
### Parsing
: 어떻게 정보를 빼서 어떻게 클래스로 만들지?
```
[
  {
    "id":1,
    "uploader":"g82",
    "text":"...", 
    "likes":0.
    "created_at":"2016-15-15T07:27:35.96ZZ", 
    "updated_at":"2016-15-15T07:27:35.96ZZ", 
    "image":{
      "url":"/uploads/post/image/2/04_-_wRFaWN5.jpg"
    }
  },
  {
  ...
  }

]

```  
## API
Application Programming Interface
* 메서드: 서로 다른 객체끼리 호출
* API: 서로 다른 앱끼리 호출 



