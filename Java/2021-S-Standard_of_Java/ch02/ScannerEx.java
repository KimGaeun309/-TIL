package ch02;

import java.util.Scanner;

public class ScannerEx {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in); // Scanner Ŭ������ ��ü�� ����
		
		System.out.print("���ڸ� ������ �ϳ� �Է����ּ���.>");
		String input = scanner.nextLine(); // �Է¹��� ������ input�� ����
		int num = Integer.parseInt(input); // �Է¹��� ���ڿ��� ���ڷ� ��ȯ
		
		System.out.println("�Է³��� : " + input);
		System.out.printf("num = %d%n", num);
	}

}
