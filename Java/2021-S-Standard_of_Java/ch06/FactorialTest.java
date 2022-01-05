package ch06;

public class FactorialTest {

	public static void main(String[] args) {
		int result = factorial(4);
		
		System.out.println(result);
	}
	
	static int factorial(int n) {
		if(n <= 0 || n > 12) return -1 // 유효성 검사 추가
		if(n==1) return 1;
		return n * factorial(n-1);
	}

}
