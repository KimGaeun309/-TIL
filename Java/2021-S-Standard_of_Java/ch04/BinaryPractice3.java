package ch04;

public class BinaryPractice3 {

	public static void main(String[] args) {
		int a=0, b=0, c=0, d=0;
		for (int i=0; i<16; i++) {		
			d = i % 2;
			c = (i / 2) % 2;
			b = (i / 4) % 2;
			a = i / 8;
			System.out.println(""+a+b+c+d);
		}
	}
}
