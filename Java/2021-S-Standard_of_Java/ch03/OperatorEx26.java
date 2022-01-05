package ch03;

public class OperatorEx26 {

	public static void main(String[] args) {
		int a = 5;
		int b = 0;
		
		System.out.printf("a=%d, b=%d%n", a, b);
		System.out.printf("a!=0 || ++b!=0 = %b%n", a!=0 || ++b!=0); // a != 0 에서 true임이 확정. 뒤의 연산은 건너뜀.
		System.out.printf("a=%d, b=%d%n", a, b);
		System.out.printf("a==0 && ++b!=0 = %b%n", a==0 && ++b!=0); // a==0 에서 false임이 확정. 뒤의 연산 건너뜀.
		System.out.printf("a=%d, b=%d%n", a, b);
	} // main의 끝

}
