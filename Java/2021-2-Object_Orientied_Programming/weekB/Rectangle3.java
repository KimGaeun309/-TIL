package weekB;
// 인터페이스 이용한 다중상속 효과

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
