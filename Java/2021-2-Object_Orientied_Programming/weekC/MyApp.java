package weekC;

import javax.swing.*;

class MyFrame extends JFrame {
	MyFrame() {
		setTitle("첫 번재 프레임");
		setSize(300, 300);
		setVisible(true);
	}
}

public class MyApp {

	public static void main(String[] args) {
		MyFrame mf = new MyFrame();
	}

}
