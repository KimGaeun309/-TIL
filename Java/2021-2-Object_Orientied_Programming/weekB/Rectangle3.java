package weekB;
// �������̽� �̿��� ���߻�� ȿ��

class Shape {
	protected int x, y;
}

interface Drawable {
	void draw();
}

public class Rectangle3 extends Shape implements Drawable {
	int width, height;
	public void draw() {
		System.out.println("Rectangle Draw");
	}
}
