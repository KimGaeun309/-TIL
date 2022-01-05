package ch03;

public class OperatorEx28 {

	public static void main(String[] args) {
		int x = 0xAB, y = 0xF;
		
		System.out.printf("x = %#X \t\t%s%n", x, toBinaryString(x));
		System.out.printf("y = %#X \t\t%s%n", y, toBinaryString(y));
		System.out.printf("%#X | %#X = %#X \t%s%n", x, y, x | y, toBinaryString(x | y));
		System.out.printf("%#X & %#X = %#X \t%s%n", x, y, x & y, toBinaryString(x & y));
		System.out.printf("%#X ^ %#X \t%s%n", x, y, x ^ y, toBinaryString(x ^ y));
		System.out.printf("%#X ^ %#X ^ %#X = %#X %s%n", x, y, y, x ^ y ^ y, toBinaryString(x ^ y ^ y));
	} // main 함수의 끝
	
	static String toBinaryString(int x) { // 10진 정수를 2진수로 변환하는 메서드
		String zero = "0000000000000000000000000000000";
		String tmp = zero + Integer.toBinaryString(x); // Integer 클래스의 toBinaryString()메서드.
		                                                   //10진수 -> 2진수 String
		return tmp.substring(tmp.length()-32); // 문자열 자르는 함수.
	}

}


