package weekB;

interface MyInterface1 {
	static void print(String msg) {
		System.out.println(msg + ": �������̽��� ���� �޼ҵ� ȣ��");
	}
}

public class StaticMethodTest {

	public static void main(String[] args) {
		MyInterface1.print("Java 8");
	}

}
