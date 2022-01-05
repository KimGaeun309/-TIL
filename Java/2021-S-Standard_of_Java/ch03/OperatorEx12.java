package ch03;

public class OperatorEx12 {

	public static void main(String[] args) {
		char c1 = 'a'; // c1에는 문자 'a'의 코드값인 97이 저장된다.
		char c2 = c1;
		char c3 = ' ';
		
		int i = c1 + 1;
		
		c3 = (char)(c1 + 1); // 연산의 결과가 int이므로 다시 형변환을 해야 함.
		c2++;
		c2++;
		
		System.out.println("i=" + i);
		System.out.println("c2=" + c2);
		System.out.println("c3=" + c3);
	}

}
