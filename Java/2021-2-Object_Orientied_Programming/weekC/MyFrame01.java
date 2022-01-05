package weekC;

// 이처럼 frame class 내에 멤버로 main을 사용하기를 권장한다.

import javax.swing.*;

public class MyFrame01 extends JFrame {
	MyFrame01() {
		setTitle("첫번째 프레임");
		setSize(300, 300);
		setVisible(true);
	}
	public static void main(String[] args) {
		MyFrame01 mf = new MyFrame01();
	}

}
