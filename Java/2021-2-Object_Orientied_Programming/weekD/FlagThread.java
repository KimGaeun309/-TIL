package weekD;

// flag�� �̿��� ����

public class FlagThread extends Thread {
	private int n = 0;
	private boolean flag = false;
	public void finish() {flag = true;}
	
	@Override
	public void run() {
		while(true) {
			System.out.println(n); // ȭ�鿡 ī��Ʈ �� ���
			n++;
			try {
				sleep(1000);
				if(flag == true)
					return; // ������ ����
			}
			catch(InterruptedException e) {
				return;
			}
		}
	}
	
	public static void main(String[] args) {
		FlagThread th = new FlagThread();
		th.start();
		
		th.finish(); // FlagThread ���� ����
	}

}
