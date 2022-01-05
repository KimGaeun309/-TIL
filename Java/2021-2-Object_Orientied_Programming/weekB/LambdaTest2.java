package weekB;

// 두 개의 인수를 받는 람다식

@FunctionalInterface
interface MyInterface4 {
	public void calculate(int x, int y);
}

public class LambdaTest2 {

	public static void main(String[] args) {
		MyInterface4 hello = (a, b) -> {
			int result = a * b;
			System.out.println("계싼 결과는 : " + result);
		};
		
		hello.calculate(10, 20);
	}

}
