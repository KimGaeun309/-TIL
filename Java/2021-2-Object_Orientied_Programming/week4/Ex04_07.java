package Week4;

// �μ��� �Ű����� ����

class Math_sum {
	int add(int x, int y) {
		return x + y;
	}
}


public class Ex04_07 {
	
	public static void main(String[] args) {
		int sum;
		Math_sum obj = new Math_sum();
		sum = obj.add(2, 3);
		System.out.println("2�� 3�� ���� " + sum);
		sum = obj.add(7, 8);
		System.out.println("7�� 8�� ���� " + sum);

	}

}
