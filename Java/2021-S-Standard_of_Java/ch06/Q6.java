package ch06;

public class Q6 {
	
	static double getDistance(int x, int y, int x1, int y1) {
		double a = (x1 - x > 0 ? x1 - x : x - x1);
		double b = (y1 - y > 0 ? y1 - y : y - y1);
		
		return Math.sqrt(a*a + b*b);
	}

	public static void main(String[] args) {
		System.out.println(getDistance(1,1,2,2));
	}

}
