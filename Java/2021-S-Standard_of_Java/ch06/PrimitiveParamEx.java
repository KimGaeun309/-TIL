package ch06;

class Data {int x;}

public class PrimitiveParamEx {

	public static void main(String[] args) {
		Data d = new Data();
		d.x = 10;
		System.out.println("main() : x = " + d.x);
		
		change(d.x);
		System.out.println("After change(d.x)");
		System.out.println("main() : x = " + d.x);
	}
	
	static void change(int x) { // 메서드의 매개변수가 기본형이라 단순히 저장된 값만을 얻어 변수의 값을 읽기만 할 수 있다.
		x = 1000;
		System.out.println("change() : x = " + x);
	}

}
