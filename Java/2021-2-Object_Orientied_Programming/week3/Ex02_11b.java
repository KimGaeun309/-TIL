package Week3;
import java.util.Scanner;

public class Ex02_11b {

	public static void main(String[] args) {
		final int TARGETSALES = 1000;
		int mySales;
		int bonus;
		String result;
		
		Scanner input = new Scanner(System.in);
		System.out.print("������ �Է��Ͻÿ�(����: ����); ");
		mySales = input.nextInt();
		
		if (mySales >= TARGETSALES) {
			result = "���� �޼�";
			bonus = (mySales - TARGETSALES) / 10;
//          bonus = (mySales - TARGETSALES) * 0.1; // Ÿ���� ���� �ʾ� ����!
			// bonus �� double�� �ٲٸ� ������ ����������!
		} else {
			result = "���� �޼� ����";
			bonus = 0;
		}
		
		System.out.println(result + "\n" + "���ʽ� : " + bonus);
		
		input.close();
	}

}
