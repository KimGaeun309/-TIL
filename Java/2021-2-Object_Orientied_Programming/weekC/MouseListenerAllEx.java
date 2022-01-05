package weekC;

// 마우스와 마우스 모션 이벤트 활용

import javax.swing.*;
import java.awt.event.*;
import java.awt.*;

public class MouseListenerAllEx extends JFrame{
	private JLabel la = new JLabel("No MouseEvent");
	
	public MouseListenerAllEx() {
		setTitle("MouseListener와 MouseMotionListener 예제");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		Container c = getContentPane();
		c.setLayout(new FlowLayout());
		
		MyMouseListener listener = new MyMouseListener();
		c.addMouseListener(listener);
		c.addMouseMotionListener(listener);
		c.add(la);
		setSize(300, 200);
		setVisible(true);
		
	}
	
	class MyMouseListener implements MouseListener, MouseMotionListener {
		public void mousePressed(MouseEvent e) {
			la.setText("MousePressed("+e.getX() + ", " + getY() + ")");
		}
		public void mouseReleased(MouseEvent e) {
			la.setText("MouseReleased("+e.getX() + ", " + getY() + ")");
		}
		public void mouseClicked(MouseEvent e) {}
		public void mouseEntered(MouseEvent e) {
			Component c = (Component)e.getSource();
			c.setBackground(Color.CYAN);
		}
		public void mouseExited(MouseEvent e) {
			Component c = (Component)e.getSource();
			c.setBackground(Color.YELLOW);
		}
		public void mouseDragged(MouseEvent e) {
			la.setText("MouseDragged("+e.getX() + ", " + getY() + ")");
		}
		public void mouseMoved(MouseEvent e) {
			la.setText("MouseMoved(" + e.getX() + ", " + e.getY() + ")");
		}
	}
	public static void main(String[] args) {
		new MouseListenerAllEx();
	}

}
