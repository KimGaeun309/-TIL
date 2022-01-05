// 2주차 - 1 - 자바 프로그램의 기본 구조

package Week2;

public class Hello { // 클래스 선언
	
	public static int sum(int n, int m) { // 메소드
		return n+m; 
	}
	public static void main(String[] args) { // main 메소드
		// 변수 선언
		int i = 20; // 초기화
		int s;
		char a;
		
		// 문장
		s = sum(i, 10); // 메소드 호출 (30 리턴)
		a = '?';
		
		// 화면 출력 - 표준 출력 스트림에 메시지 출력
		System.out.println(a);
		System.out.println("Hello");
		System.out.println(s);
	}
}

