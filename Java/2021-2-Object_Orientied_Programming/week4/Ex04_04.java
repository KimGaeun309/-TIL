package Week4;

public class Ex04_04 {
	static int a = 100;
	
	static void func1() {
		int a = 200;
		System.out.printf("func1에서 a의 값 ==> %d\n", a);
	}
	
	public static void main(String[] args) {
		func1();
		System.out.printf("main() 에서의 a의 값 ==> %d\n", a);

	}

}
