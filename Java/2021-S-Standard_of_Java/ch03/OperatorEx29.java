package ch03;

public class OperatorEx29 {

	public static void main(String[] args) {
		byte p = 10;
		byte n = -10;
		
		System.out.printf(" p  =%d \t%s%n", p, toBinaryString(p));
		System.out.printf("~p  =%d \t%s%n", ~p, toBinaryString(~p));
		System.out.printf("~p+1=%d \t%s%n", ~p+1, toBinaryString(~p+1));
		System.out.printf("~~p =%d \t%s%n", ~~p, toBinaryString(~~p)); // ~~p 연산결과의 타입이 byte가 아니라 int.
		System.out.println();// 비트 전환 연산자는 피연산자의 타입이 int보다 작으면 int로 자동 형변환(산술변환) 후에 연산하기 때문.
		System.out.printf(" n  =%d%n", n);                          // 따라서 결과로 32자리의 2진수가 나온다.
		System.out.printf("~(n-1)=%d%n", ~(n-1));
	} // main의 끝
	
	// 10진 정수를 2진수로 변환하는 메서드
	static String toBinaryString(int x) {
		String zero = "00000000000000000000000000000000";
		String tmp = zero + Integer.toBinaryString(x);
		return tmp.substring(tmp.length()-32);
	}

}
