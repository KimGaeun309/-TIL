package Week2;
import java.util.Scanner;

public class TestNextLine {

	public static void main(String[] args) {
		System.out.println("ù��° ���ڿ��� �Է��ϼ���");
		Scanner scanner = new Scanner(System.in);
		
		String input = scanner.nextLine(); // ���ڿ� �б�
		System.out.println("input: " + input);
		
		System.out.println("�ι�° ���ڿ��� �Է��ϼ���");
		
		String input1 = scanner.next(); // ���ڿ� �б�
		System.out.println("input1: " + input1);
		
		String input2 = scanner.next(); // ���ڿ� �б�
		System.out.println("input2: " + input2);
		
		scanner.close();
	}

}
