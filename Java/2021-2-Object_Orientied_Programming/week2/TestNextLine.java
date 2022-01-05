package Week2;
import java.util.Scanner;

public class TestNextLine {

	public static void main(String[] args) {
		System.out.println("첫번째 문자열을 입력하세요");
		Scanner scanner = new Scanner(System.in);
		
		String input = scanner.nextLine(); // 문자열 읽기
		System.out.println("input: " + input);
		
		System.out.println("두번째 문자열을 입력하세요");
		
		String input1 = scanner.next(); // 문자열 읽기
		System.out.println("input1: " + input1);
		
		String input2 = scanner.next(); // 문자열 읽기
		System.out.println("input2: " + input2);
		
		scanner.close();
	}

}
