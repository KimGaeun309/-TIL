package Week3;
import java.util.Scanner;

public class Ex02_11a {

	public static void main(String[] args) {
		int x, y, max;
		
		Scanner input = new Scanner(System.in);
		System.out.print("ù��° ����: ");
		
		x = input.nextInt();
		
		System.out.print("�ι�° ����: ");
		y = input.nextInt();
		
		if (x > y)
			max = x;
		else
			max = y;
//      max = (x > y) ? x : y; // ���� ������
		
		System.out.println("ū ���� " + max);
		
		input.close();
	}

}
