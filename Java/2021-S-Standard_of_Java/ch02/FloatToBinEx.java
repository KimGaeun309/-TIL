package ch02;

public class FloatToBinEx {

	public static void main(String[] args) {
		float f = 9.1234567f;
		int i = Float.floatToIntBits(f); // float타입의 값을 int타입의 값으로 해석해서 반환하는 함수.
		
		System.out.printf("%f%n", f);
		System.out.printf("%X%n", i); // 16진수로 출력
	}

}
