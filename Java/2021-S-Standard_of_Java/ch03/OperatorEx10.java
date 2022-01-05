package ch03;

public class OperatorEx10 {

	public static void main(String[] args) {
		int a = 1000000;
		
		int result1 = a * a / a; // 먼저 곱하면 int의 범위를 넘어서 오버플로우 발생해 다른 결과가 나옴.
		int result2 = a / a * a;
		
		System.out.printf("%d / %d %d%n", a, a, a, result1);
		System.out.printf("%d / %d * %d", a, a, a, result2);
	}

}
