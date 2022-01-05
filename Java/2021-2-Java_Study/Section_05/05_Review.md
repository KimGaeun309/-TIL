# Section 05
## Data to Object
데이터는 정보 그 자체.
### 1단계
* 필요한 자료는?
  + 업로더 프로필사진(이미지), 업로더(글자)
  + 본문 사진(이미지)  
  + 좋아요 수(숫자)
  + 글 내용(글자)
  + 덧글 갯수(숫자)
  + 올린 시간(시간)
### 2단계
* 1단계에서 뽑아낸 자료들을 클래스로 만들기 (디지털화)
```java
public class DataUserPost {
  String userPhotoUrl; // 업로더 프로필 사진(이미지) -> url로 저장했다가 필요할 때만 다운로드
  String userNickname; // 업로더(숫자)
  
  String postPhotoUrl; // 본문 사진(이미지)
  String postText; // 글 내용(글자)
  
  int likeCount; // 좋아요 수(숫자)
  int replyCount; // 덧글 개수(숫자)
  
  Date uploadDate; // 올린 시간(시간)
}

```
### 일단 코드로 입력해보자
* 직접 코드로 입력 - 테스트용
* 서버에서 제공 - 실제 서비스

## Collections
### 배열의 번거로움
* 도중에 삽입하기 번거로움
* 값을 이어붙이기 번거로움
* 한번만 만들어놓고 유연하게 수정&확장하면서 응용하기가 어렵다
-> 이를 보완하는 자료구조들 많음
### List (linked list)
* 중간에 값 삽입 가능.
* 중간에 값 제거 가능.
* 늘 연결되어서 수정&확장하면서도 여전히 값 순회하기 편함
**ArrayList 생성**
``` java
private void makeArrayList() {
  ArrayList<DataUserPost> arrayList = new ArrayList<>();
  arrayList.add(new DataUserPost());
  arrayList.add(1, new DataUserPost());
  arrayList.remove(1);
  DataUserPost dataUserPost = arrayList.get(2);
}
```
**ArrayList 2가지 순회법**
``` java
ArrayList<DataUserPost> arrayList = new ArrayList();
for(int i=0; i<arrayList.size(); i++) {
  DataUserPost data = arrayList.get(i);
  System.out.println(data.toString());
}
```
``` java
ArrayList<DataUserPost> arrayList = new ArrayList();
for(DataUserPost data : arrayList) {
  System.out.println(data.toString());
}
```

## RecyclerView
### RecyclerView
기존의 ListView, GridView에서의 구현의 불편함과 최적화를 잠아낸 AdapterView 기본으로 제공되지 않고 서포트 라이브러리 형태로 존재한다.
우리가 보통 쓰는 페이스북이나 인스타그램의 많은 타임라인 등이 이걸로 구현된다.
### LayoutManager
* LinearLayoutManager (리스트 뷰)
* GridLayoutManager (그리드 뷰)
* StaggeredGridLayoutManager (엇갈린 그리드 뷰)

### 프로젝트에 추가하기
support library 
```
complie 'com.android.support:recyclerview-v7:23.3.0'
```

## RecyclerView, ViewHolder
### Cache
많이 쓰이거나 쓰일 것이라 예상되는 것들을 빨리 찾아쓸 수 있는 곳에 미리 배치해두는 것

### VirewHolder
findViewById()는 생각보다 댓가가 큰 메소드이다. (cpu 사용 용량 큼)
그래서 미리 View들을 다 찾아놓고 캐시해둔 뒤에 재활용하기 위하여 만들어진 것.

## RecyclerView.Adapter
### Adapter<뷰홀더>
<뷰홀더>를 갖고 있는 어댑터. 
<> 안에 자신이 정의한 뷰홀더를 넣거나
여러 형태의 뷰를 넣고 싶다면 <RecyclerView.ViewHolder>를 넣자
``` java
class PostAdapter extends RecyclerView.Adapter<PostViewHolder> {
  @Override
  public PostViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {
    return null;
  }
  
  @Override
  public void onBindViewHolder(PostViewHolder holder, int position) {
    
  }
  
  @Override
  public int getItemCount() {
    return 0;
  }
}

```


