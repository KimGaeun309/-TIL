package weekA;
import java.util.Scanner;

public class DivideByZero {
	
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int dividend; // ������
		int divisor; // ������
		while(true) {
			System.out.print("�������� �Է��Ͻÿ�");
			dividend = scanner.nextInt();
			System.out.print("�������� �Է��Ͻÿ�"); // 0 �Է��ϸ� Arithmetic Exception �߻�
			divisor = scanner.nextInt();
			try {
				System.out.println(dividend + " �� " + divisor + "�� ������ ���� " + dividend/divisor + "�Դϴ�.");
				break;
			}
			catch(ArithmeticException e) {
				System.out.println("0���� ���� �� �����ϴ�! �ٽ� �Է�������");
			}
		}
		
		scanner.close();
	}

}
