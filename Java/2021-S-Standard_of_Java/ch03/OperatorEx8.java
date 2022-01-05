package ch03;

public class OperatorEx8 {

	public static void main(String[] args) {
		long a = 1_000_000 * 1_000_000; // 연산결과가 int라서 이미 오버플로우가 발생했기 때문에.
		long b = 1_000_000 * 1_000_000L; // 연산결과가 long타입.
		
		System.out.println("a=" + a);
		System.out.println("b=" + b);
	}

}
