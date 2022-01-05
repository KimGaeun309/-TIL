package ch06;

class MyPoint {
	int x;
	int y;
	
	MyPoint(int x, int y) { 
		this.x = x;
		this.y = y;
	}
	
	double getDistance(int x1, int y1) {
		double a = (x1 - x > 0 ? x1 - x : x - x1);
		double b = (y1 - y > 0 ? y1 - y : y - y1);
		
		return Math.sqrt(a*a + b*b);
	}
}
public class Q7 {

	public static void main(String[] args) {
		MyPoint p = new MyPoint(1, 1);
		
		
		System.out.println(p.getDistance(2, 2));
	}

}
