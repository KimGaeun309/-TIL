package weekD;

public class AnonymousThreadTimer {

	public static void main(String[] args) {
		// 익명 자식 객체 만들어 사용
		Thread th = new Thread() {
			int n = 0;
			@Override
			public void run() {
				while(true) {
					System.out.println(n);
					n++;
					try {
						Thread.sleep(1000);
					}
					catch (InterruptedException e) {
						return;
					}
				}
			}
		};
		th.start();
	}

}
