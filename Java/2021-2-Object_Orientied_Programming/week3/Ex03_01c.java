package Week3;
// ������ �� ���
import java.util.Random;
import java.util.Scanner;

public class Ex03_01c {

	public static void main(String[] args) {
		
		Random generator = new Random();
		
		System.out.print("������ ����: ");
		Scanner scan = new Scanner(System.in);
		int count = scan.nextInt();
		int sum = 0;
		
		for (int i=0; i<count; i++) {
			int number = generator.nextInt(100);
			System.out.println("������ ���� " + number);
			sum += number;
		}
		System.out.print("���� " + count + "���� ���� " + sum);
		scan.close();

	}

}
