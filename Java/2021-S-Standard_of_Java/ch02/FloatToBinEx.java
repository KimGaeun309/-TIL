package ch02;

public class FloatToBinEx {

	public static void main(String[] args) {
		float f = 9.1234567f;
		int i = Float.floatToIntBits(f); // floatŸ���� ���� intŸ���� ������ �ؼ��ؼ� ��ȯ�ϴ� �Լ�.
		
		System.out.printf("%f%n", f);
		System.out.printf("%X%n", i); // 16������ ���
	}

}
