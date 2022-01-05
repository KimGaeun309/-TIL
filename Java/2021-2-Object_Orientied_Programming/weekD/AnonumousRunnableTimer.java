package weekD;

// Runnable 익명 구현 객체 이용

public class AnonymousRunnableTimer {

	public static void main(String[] args) {
		Thread th = new Thread(new Runnable() {
			int n = 0;
			
			@Override
			public void run() {
				while(true) {
					System.out.println(n);
					n++;
					try {
						Thread.sleep(1000);
					}
					catch(InterruptedException e) {
						return;
					}
				}
			}
		});
		th.start();
	}

}
