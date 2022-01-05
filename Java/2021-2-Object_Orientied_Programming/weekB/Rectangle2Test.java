package weekB;

public class Rectangle2Test {

	public static void main(String[] args) {
		Rectangle2 r1 = new Rectangle2(100, 30);
		Rectangle2 r2 = new Rectangle2(200, 10);
		int result = r1.compareTo(r2);
		if (result == 1)
			System.out.println(r1 + "가 더 큽니다.");
		else if (result == 0)
			System.out.println("같습니다.");
		else
			System.out.println(r2 + "가 더 큽니다.");
	}

}
