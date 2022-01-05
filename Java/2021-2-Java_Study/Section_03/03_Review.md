# Section 03
## 안드로이드 View
### View (class 로 되어 있음)
* 화면 그 자체
* Activity에 씌우는 화면 껍데기(보통 XML 파일에 저장)
* XML, Java 둘 중 하나로작성가능 (보통 XML)
* 보통 Widget, Adapter, Layout 계열로 나눌 수 있다. (공식적인 분류는 아님)
### Widget
* TextView, ImageView 등...
* 보통 사용자와 작용하는 용도가 뚜렷한 View들
### Adapter
* ListView, GridView, RecyclerView 등...
* 많은 정보를 길게 스크롤하며 나열할 때 많이 씀
### Layout
* LinearLayout, RelativeLayout, FrameLayout 등...
* Widget, Adapter, Layout 을 담을 수 있는 틀
* 화면 공간을 배분할 때 많이 쓰인다.
### XML
Widget, Adapter, Layout 모두 XML 로 외형을 판단
``` XML
<View
      android:layout_width="match_parent"
      android:layout_height="wrap_content"
      android:background="#ff0000"
      >
  <TextView ... />
  <ImageView ... />
</View>
```
위 코드에서 width, height 는 무조건 필요함.

## View Widget (목적이 뚜렷한 게 특징)
### TextView (글자)
``` XML
<TextView
          android:layout_width="match_parent"
          android:layout_height="wrap_content"
          android:text="주모오오오-----!!"
          />                       
```
### ImageView (이미지)
``` XML
<ImageView
          android:layout_width="match_parent"
          android:layout_height="wrap_content"
          android:src="R.drawable.XXX" <!--android:src="@drawable/irene"-->
          android:scaleType="centerCrop"
          />
```
res 폴더 안에 drawable 폴더 안에 이미지 파일이 있는데 확장자 (.png) 쓰지 않아도 된다.

## View Layout 
### LinearLayout (선형 레이아웃. 순차적으로..)
``` XML
<LinearLayout
              android:orientation="vertical"/>
<!--android:orientation="horizontal"-->
```
### RelativeLayout (관계 정의.)
``` XML
<RelativeLayout>
      <Button
         android:id="@+id/btn_toast"
         />
      
      <ImageView
          android:layout_above="@id/btn_toast"
          android:id="@+id/iv_photo"
          />
</RelativeLayout>
```
### FrameLayout 
``` XML
<FrameLayout>
      <Button
         android:layout_gravity="bottom"
         />
      
      <ImageView
          android:layout_gravity="center"
          />
</FrameLayout>
```
layout_gravity 는 LinearLayout에도 있지만 그와 달리 FrameLayout 에서는 겹칠 수도 있다.

## View Event
### event driven (언제 발생할지 모를 것들)
* 안드로이드의 이벤트(콜백)
   + 버튼을 눌렀다
   + Back key를 눌렀다
   + 인터넷이 끊겼다
   + 터치를 했다
   + 화면을 가로로 뒤집었다
* 우리에게는 오지 않을 이벤트
   + 카톡이 왔다
   + 문자가 왔다
   + 전화가 왔다
   + 배터리가 매우 부족하다
### Listener
어떤 이벤트가 발생했다고 알려준다
``` java
public interface OnLifeListener {
      void onLife(boolean isSiljeon);
}
```
Listener는 인터피이스이고 결국 콜백이다 (콜백은 2-I 실습은 2-J)



