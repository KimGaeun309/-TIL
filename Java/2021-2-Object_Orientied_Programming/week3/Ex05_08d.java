package Week3;
import java.util.Scanner;
import java.util.Random;

public class Ex05_08d {
	final int SCISSOR = 0;
	final int ROCK = 1;
	final int PAPER = 2;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		Random ran = new Random();
		
		System.out.print("����(0), ����(1), ��(2)");
		int user = sc.nextInt();
		
		int computer = ran.nextInt(3);
		
//      int computer = (int)(Math.random() * 3); // random()�� 0.0~1.0 �� double �� �� ��ȯ.
		
		if(user == computer)
			System.out.println("�ΰ��� ��ǻ�Ͱ� �����");
		
		// else if(user == (computer + 1) % 3)
		else if((user == 0 && computer == 2) || (user == 1 && computer == 0) || (user == 2 && computer == 1))
			System.out.println("�ΰ�: " + user + "��ǻ��: " + computer + " �ΰ� �¸�");
		else
			System.out.println("�ΰ�: " + user + "��ǻ��: " + computer + " ��ǻ�� �¸�");

		sc.close();
	}

}
