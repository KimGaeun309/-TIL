package Week6;

class OuterClass {
	private int value = 10;
	
	class InnerClass {
		public void myMethod() {
			 System.out.println("�ܺ� Ŭ������ private ���� ��: " + value);
		}
	}
	
	OuterClass() {
		InnerClass obj = new InnerClass();
		obj.myMethod();
	}
}

public class InnerClassTest {

	public static void main(String[] args) {
		OuterClass outer = new OuterClass();
	}

}
