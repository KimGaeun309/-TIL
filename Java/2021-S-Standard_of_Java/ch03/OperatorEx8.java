package ch03;

public class OperatorEx8 {

	public static void main(String[] args) {
		long a = 1_000_000 * 1_000_000; // �������� int�� �̹� �����÷ο찡 �߻��߱� ������.
		long b = 1_000_000 * 1_000_000L; // �������� longŸ��.
		
		System.out.println("a=" + a);
		System.out.println("b=" + b);
	}

}
