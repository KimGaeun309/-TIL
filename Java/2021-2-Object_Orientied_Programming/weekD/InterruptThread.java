package weekD;

public class InterruptThread extends Thread {
	private int n = 0;
	
	@Override
	public void run() {
		while(true) {
			System.out.println(n); // ȭ�鿡 ī��Ʈ �� ���
			n++;
			try {
				sleep(1000);
			}
			catch(InterruptedException e) {
				return; // ���ܸ� �ް� ������ �����Ͽ� ����
			}
		}
	}
	
	public static void main(String[] args) {
		InterruptThread th = new InterruptThread();
		th.start();
		
		th.interrupt(); // InterruptThread ��������
		  // --> main �������� interrupt() �޼ҵ� ȣ�⿡ ����
		     // catch�� ����. �׸��� ����.
	}

}
