package weekB;
// �Ű������� ������ �ʴ� ���ٽ�

@FunctionalInterface 
interface MyInterface2 {
	void sayHello();
}
public class LambdaTest1 {

	public static void main(String[] args) {
		MyInterface2 hello = () -> System.out.println("Hello, lambda!");
		hello.sayHello();
	}

}
