package Week3;
import java.util.Scanner;

public class Ex02_15a {

	public static void main(String[] args) {
		int month;
		int days = 0;
		
		System.out.print("�ϼ��� �˰� ���� ���� �Է��Ͻÿ�: ");
		Scanner scan = new Scanner(System.in);
		
		month = scan.nextInt();
		switch (month) {
		case 4:
		case 6:
		case 11:
			days = 30;
			break;
		case 2:
			days = 28;
			break;
			default:
				days = 31;
		}
		System.out.println("���� ������ " + days);
		
		scan.close();

	}

}
