package ch03;

public class OperatorEx22 {

	public static void main(String[] args) {
		float f = 0.1f;
		double d = 0.1;
		double d2 = (double)f;
		
		System.out.printf("10.0==10.0f  %b%n", 10.0 == 10.0f); // true
		System.out.printf("0.1==0.1f    %b%n", 0.1 == 0.1f); // false (float에서 더 큰 오차가 발생하기 때문.)
		System.out.printf("f = %19.17f%n", f);
		System.out.printf("d = %19.17f%n", d);
		System.out.printf("d2=%19.17f%n", d2);
		System.out.printf("d==f  %b%n", d==f); // false
		System.out.printf("d==d2 %b%n", d==d2); // false
		System.out.printf("d2==f %b%n", d2==f); // true
		System.out.printf("(float)d==f %b%n", (float)d==f); // true
	}

}
// float 값과 double 값을 비교하려면 double타입의 값을 float타입으로 형변환한 다음에 비교해야 한다!!