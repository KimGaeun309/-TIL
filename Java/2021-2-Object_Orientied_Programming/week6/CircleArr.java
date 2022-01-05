package Week6;

public class CircleArr {
	int radius;
	public CircleArr(int radius) {
		this.radius = radius;
	}
	public double getArea() {
		return 3.14 * radius * radius;
	}

	public static void main(String[] args) {
		CircleArr [] c;
		c = new CircleArr[5];
		
		for(int i=0; i<c.length; i++)
			c[i] = new CircleArr(i);
		
		for(int i=0; i<c.length; i++)
			System.out.print((int)(c[i].getArea()) + " ");
	}

}
