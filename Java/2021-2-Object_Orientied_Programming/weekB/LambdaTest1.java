package weekB;
// 매개변수를 가지지 않는 람다식

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
