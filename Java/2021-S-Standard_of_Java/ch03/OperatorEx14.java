package ch03;

public class OperatorEx14 {

	public static void main(String[] args) {
		char c = 'a';
		for(int i=0; i<26; i++) {
			System.out.print(c++);
		}
		System.out.println();
		
		c = 'A';
		for(int i=0; i<26; i++) {
			System.out.print(c++);
		}
		System.out.println();
		
		c = '0';
		for(int i = 0; i<10; i++) {
			System.out.print(c++);
		}
		System.out.println();
	}

}

// println메서드는 값을 출력하고 줄을 바꾸지만, print메서드는 줄을 바꾸지 않고 출력한다.