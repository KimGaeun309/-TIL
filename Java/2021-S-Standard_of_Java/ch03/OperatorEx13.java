package ch03;

public class OperatorEx13 {

	public static void main(String[] args) {
		char c1 = 'a';
		
		//char c2 = c1 + 1; // 컴파일 에러 발생
		char c2 = 'a' + 1; // 컴파일 에러 없음. 
		//리터럴 간의 연산이기 때문에 컴파일 시에 컴파일러가 계산해서 그 결과로 대체함으로써 코드를 보다 효율적으로 만든다.
		
		System.out.println(c1 + c2);
	}

}
