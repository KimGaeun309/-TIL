package weekD;

// Thread Ŭ������ ������ ����

/* Thread Ŭ������ ����ϴ� ���
 Thread Ŭ������ ��ӹ��� �Ŀ� run() �޼ҵ带 �������Ѵ�.
 run() �޼ҵ� �ȿ� �۾��� ����Ѵ�.
*/

class MyThread extends Thread {
	@Override
	public void run() {
		for (int i=10; i>=0; i--) {
			System.out.print(i + " ");
		}
	}
}

public class MyThreadTest {

	public static void main(String[] args) {
		Thread t = new MyThread();
		t.start();
	}

}
