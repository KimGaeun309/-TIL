package ch04;

public class BinaryPractice2 {
	public static void main(String[] args) {
		int a=0, b=0, c=0, d=0;
		for (;;) {
			System.out.println(""+a+b+c+d);
			
			if (d+c+b+a == 4) {
				break;
			} else if (d+c+b == 3) {
				a = (a + 1) % 2;
				b = 0; c = 0; d = 0;
			} else if (d+c == 2) {
				b = (b + 1) % 2;
				c = 0; d = 0;
			} else if (d == 1) {
				c = (c + 1) % 2;
				d = 0;
			} else {
				d = (d + 1) % 2;
			}
		}
	}
}
