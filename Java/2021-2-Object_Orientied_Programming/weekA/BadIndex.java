package weekA;

public class BadIndex {

	public static void main(String[] args) {
		int[] array = new int[10];
		for(int i=0; i<10; i++)
			array[i] = 0;
		try {
			int result = array[12];
		} catch (ArrayIndexOutOfBoundsException e) {
			System.out.println("�迪�� �ε��� �߸���");
		}
		
		//int result = array[12]; // ArrayIndexOutOfBoundsException
		System.out.println("���� �� ������ ����ɱ��?");
		// ����ó���� ���־��⶧���� �� ������ ����˴ϴ�.

	}

}
