package ch03;

public class OperatorEx10 {

	public static void main(String[] args) {
		int a = 1000000;
		
		int result1 = a * a / a; // ���� ���ϸ� int�� ������ �Ѿ �����÷ο� �߻��� �ٸ� ����� ����.
		int result2 = a / a * a;
		
		System.out.printf("%d / %d %d%n", a, a, a, result1);
		System.out.printf("%d / %d * %d", a, a, a, result2);
	}

}
