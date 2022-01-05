package ch03;

public class OperatorEx6 {

	public static void main(String[] args) {
		byte a = 10;
		byte b = 20;
		byte c = a + b; // 컴파일 에러 발생. int형으로 변환해 덧셈 수행하기 때문에 byte 자료형의 변수에 저장하려면 형변환시켜야 함.
		System.out.println(c);
	}

}
